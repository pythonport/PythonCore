'''
Created on Jan 18, 2021
Write a program to get http request information
from url www.ted.com and open it from within
your program
@author: admin
'''
import urllib.request
import webbrowser
weburl = urllib.request.urlopen('https://www.ted.com/')
html = weburl.read()
data = weburl.getcode()
url = weburl.geturl()
hd = weburl.headers
info = weburl.info()
print("The url is - ", url)
print("HTTP status code is - ", data)
print('Header returned \n', hd)
print('The info() returns \n', info)
print('Now opening the url', url)
webbrowser.open_new("https://www.ted.com/")
