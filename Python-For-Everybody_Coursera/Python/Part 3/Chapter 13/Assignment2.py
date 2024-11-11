import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

uh=urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()

try:
    info = json.loads(data)
except:
    info=None

if not info :
    print('---Failed to Retrieve---\r\n-----Quitting-----')
    quit()

print('Retrieved', len(data), 'characters')

sum=0
for item in info['comments']:
    sum=sum+item['count']

print('Count:',len(info['comments']))
print('Sum:',sum)
