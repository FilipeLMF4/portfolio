import urllib.request, urllib.parse, urllib.error

url=input('Enter URL: ')

try:
    html = urllib.request.urlopen(url)

except:
    print('Invalid URL')
    quit()

count=0
cont = html.read()
print(cont[:3000].decode().strip())
print('\r\n\r\nNumber of Characters:',len(cont))
