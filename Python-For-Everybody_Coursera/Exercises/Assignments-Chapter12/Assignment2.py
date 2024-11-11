import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

count = input('Enter count: ')
pos = input('Enter position: ')

count=float(count)
pos=float(pos)

j=0
print('Retrieving:', url)
while j<count :
    i=0
    for tag in tags:
        i=i+1
        if i==pos :
            html = urllib.request.urlopen(tag.get('href',None), context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            print('Retrieving:', tag.get('href', None))
            break
    j=j+1

print('Last name:', tag.contents[0])
