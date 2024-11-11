from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum= 0
count=0

tags = soup('span')
for tag in tags:
    numf=float(tag.contents[0])
    sum=sum+numf
    count=count+1

print('Count', count)
print('Sum', int(sum))
