'''
Created on Sep 10, 2021

@author: admin
'''
import urllib
import urllib.request

import webbrowser

weburl1 = urllib.request.urlopen("http://pythonport.com")
html = weburl1.read()
data = weburl1.getcode()
urlPath = weburl1.geturl()
header = weburl1.headers
info = weburl1.info()
print(html)
print("===============")
print(data)
print("===============")
print(urlPath)
print("===============")
print(header)
print("===============")
print(info)
print("===============")
webbrowser.open(urlPath)
