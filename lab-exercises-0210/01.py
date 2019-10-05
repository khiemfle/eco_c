__author__ = 'root'
import urllib2

body = urllib2.urlopen("http://10.0.2.15:81")
print body.read()