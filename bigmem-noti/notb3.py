from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


import datetime
import json
import shutil
import getpass
import sys
import hashlib
import base64
import schedule
import time

def get_firefox_options():
    options = Options()
    options.headless = True
    options.add_argument('window-size=2048x1080')
    return options

def login_to_bigmem(username, pwd, firefox_path):
    # Ref from: https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python
    binary = FirefoxBinary(firefox_path)
    # Ref from https://medium.com/ananoterminal/install-selenium-on-windows-f4b6bc6747e4
    browser = Firefox(firefox_binary=binary, options=get_firefox_options())
    browser.get("https://bigmem.item.ntnu.no/index.php?page=login")
    page = browser.page_source

    print(page)

    wait = WebDriverWait(browser, 30)

    return browser

# login_to_bigmem("", "", "/media/e/Workspace/Ntnu/Linux/Ethical/eco_c/bigmem-noti/firefox/firefox", "/media/e/Workspace/Ntnu/Linux/Ethical/eco_c/bigmem-noti/geckodriver")
login_to_bigmem("", "", sys.argv[1])