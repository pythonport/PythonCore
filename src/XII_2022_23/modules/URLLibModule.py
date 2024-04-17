'''
Created on Aug 27, 2022

@author: admin
'''
import urllib as urllib
import urllib.request
import webbrowser as wb
weburl = urllib.request.urlopen('https://www.tesusoft.com/')
html = weburl.read()
data = weburl.getcode()
url = weburl.geturl()
hd = weburl.headers
info = weburl.info()
print('The url is - ',url)
print('===============================')
print('HTTP Status code - ',data)
print('===============================')
print('Header returns - \n',hd)
print('===============================')
print('the Info() returns - \n',info)
print('===============================')
print('HTML Source code is - \n',html)
print('===============================')
print('Opening the url - ',url)

wb.open_new(url)