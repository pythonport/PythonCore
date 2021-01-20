'''
Created on Jul 12, 2019

@author: admin
'''
import urllib.request as req
import webbrowser
weburl = req.urlopen("http://pythonport.com")
html = weburl.read()
data  = weburl.getcode()
url = weburl.geturl()
hd = weburl.headers
inf = weburl.info()

print('The url is - ',url)
print('http response coe - ',data)
print('Headers returned  - \n',hd)
print('the info() is - \n',inf)
print('Now opening the url')
webbrowser.open(url)