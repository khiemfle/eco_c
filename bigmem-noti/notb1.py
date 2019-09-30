from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cryptography.fernet import Fernet

import requests
import datetime
import json
import shutil
import getpass
import sys
import hashlib
import base64
import schedule
import time

def get_chrome_options():
	options = ChromeOptions()
	# prefs = {"profile.default_content_settings.popups":0}
	# options.add_argument("user-data-dir=" + "C:\\Users\\timo\\PycharmProjects\\CostHistory")
	options.add_argument("headless")
	options.add_argument('window-size=2048x1080')
	# options.add_experimental_option("prefs", prefs)
	return options

def login_to_cloudhealth(email, pwd):
	browser = Chrome(chrome_options=get_chrome_options())
	browser.get("https://apps.cloudhealthtech.com/login")
	page = browser.page_source
	soup = BeautifulSoup(page, 'html.parser')

	wait = WebDriverWait(browser, 30)
	wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@ng-click="gdprAccepted()"]')))

	# print(browser.find_element_by_xpath('//button[@ng-click="gdprAccepted()"]'))
	# Next page
	browser.find_element_by_xpath('//button[@ng-click="gdprAccepted()"]').click()

	browser.find_element_by_id('email_input').send_keys(email)
	print(browser.find_element_by_id('login_button').text)
	browser.find_element_by_id('login_button').click()
	wait = WebDriverWait(browser, 30)
	wait.until(EC.visibility_of_element_located((By.ID, 'password_input')))

	browser.find_element_by_id('password_input').send_keys(pwd)
	browser.find_element_by_id('login_button').click()
	wait = WebDriverWait(browser, 60)

	return browser


def generate_report(browser, datatable_url, datatable_file_name, chart_url, chart_file_name):
	# Generate chart
	browser.get(chart_url)
	wait = WebDriverWait(browser, 60)

	canvas = browser.find_element_by_tag_name("img")
	canvas.screenshot(chart_file_name)

	# Generate data table
	browser.get(datatable_url)
	wait = WebDriverWait(browser, 200)
	wait.until(EC.visibility_of_element_located((By.ID, 'bootgrid_contents')))
	# print(browser.find_element_by_id("master_table_container2").get_attribute("height"))

	# A little modification to make the data table fully available
	browser.execute_script("document.getElementsByClassName('bootgrid-table-wrapper')[0].setAttribute('style', 'max-height:none; overflow:hidden')")
	canvas = browser.find_element_by_xpath('//div[@class="bootgrid-table-wrapper"]')
	canvas.screenshot(datatable_file_name)

def read_links(links_file):
	# Return an array of dicts
	with open(links_file) as json_file:  
		data = json.load(json_file)
		return data['links']


def decrypt(passphrase, credential_file):
	# return {email, password}
	passphrase_bytes = passphrase.encode('utf-8')
	key = base64.urlsafe_b64encode(hashlib.sha256(passphrase_bytes).digest())
	f = Fernet(key)

	with open(credential_file, 'rb') as file_reader:
		cipher_text = file_reader.read()
	temp = f.decrypt(cipher_text)
	# print(temp)
	plain_text = temp.decode('utf-8')
	# print(plain_text)
	return json.loads(plain_text)

def encrypt(passphrase, email, pwd, credential_file):
	# Save encrypted data to the crendential_file
	passphrase_bytes = passphrase.encode('utf-8')
	key = base64.urlsafe_b64encode(hashlib.sha256(passphrase_bytes).digest())
	f = Fernet(key)
	plain_text = '{{ "email": "{}", "pwd" : "{}" }}'.format(email, pwd)
	cipher_text = f.encrypt(plain_text.encode('utf-8'))
	with open(credential_file, 'wb') as file_writer:
		file_writer.write(cipher_text)

def generate_imgs(report_chart_links):
	print("generate_imgs")
	for report_chart_link in report_chart_links:
		generate_report(browser, report_chart_link['datatable_url'], report_chart_link['datatable_file_name'], report_chart_link['chart_url'], report_chart_link['chart_file_name'])


# Sample command:
# cred init
# cred passphrase
# cred info
# generate 'C:\links.json'

if sys.argv[1] == 'cred':
	if sys.argv[2] == 'init':
		new_email = input("Email: ")
		new_pwd = getpass.getpass("Password: ")
		passphrase = getpass.getpass('Passphrase: ')

		encrypt(passphrase, new_email, new_pwd, 'credential_file')

	elif sys.argv[2] == 'passphrase' or sys.argv[2] == 'info':
		current_passphrase = getpass.getpass('Current passphrase: ')
		try:
			cred = decrypt(current_passphrase, 'credential_file')

			if sys.argv[2] == 'passphrase':
				passphrase = getpass.getpass('Passphrase: ')

				encrypt(passphrase, cred['email'], cred['pwd'], 'credential_file')
			elif sys.argv[2] == 'info':
				new_email = input("Email: ")
				new_pwd = getpass.getpass("Password: ")

				encrypt(current_passphrase, new_email, new_pwd, 'credential_file')
		except Exception as e:
			raise e

elif sys.argv[1] == 'generate':
	# Flow
	passphrase = getpass.getpass('Passphrase: ')
	cred = decrypt(passphrase, 'credential_file')
	browser = login_to_cloudhealth(cred['email'], cred['pwd'])

	report_chart_links = read_links(sys.argv[2])

	schedule.every().day.at("6:30").do(lambda: generate_imgs(report_chart_links))

	while True:
		schedule.run_pending()