import urllib2

url = "http://10.0.2.15:81"

headers = {}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()