from urllib import request
from bs4 import BeautifulSoup

url = 'http://news.sohu.com/'

rsp = request.Request(url)
rsp = request.urlopen(rsp)
html = rsp.read()

soup = BeautifulSoup(html,'html.parser')
content= soup.prettify()
print(type(soup.head))
print(type(soup.head.contents))
print(soup.head)
print(soup.head.contents)
for node in soup.head:
    print(node)
    print('='*12)