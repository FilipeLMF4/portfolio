import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    api_key = False
    address = input('Enter location: ')
    if len(address) < 1:
        break

    typ = input('Enter type of data (1.XML or 2.JSON): ')
    try:
        typ=int(typ)
    except:
        break

    if typ != 1 and typ != 2 :
        print('---Invalid type of data---\r\n-----Quitting-----')
        break

    if typ == 2 :
        if api_key is False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/json?'
        else :
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

        parms = dict()
        parms['address'] = address
        if api_key is not False:
            parms['key'] = api_key

        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        #print(json.dumps(js, indent=4))

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)

        pos=0
        check = False
        for item in js['results'][0]['address_components'] :
            for info in item.get('types',None) :
                if info == 'country' :
                    check = True
                    break)
            if check == True :
                break
            pos=pos+1

        if len(js['results'][0]['address_components']) < pos+1 or 'short_name' not in js['results'][0]['address_components'][pos] :
            print('No Country code found')
            continue

        code = js['results'][0]['address_components'][pos]['short_name']
        print('Country code:',code)

    else :
        if api_key is False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
        else :
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

        parms = dict()
        parms['address'] = address
        if api_key is not False:
            parms['key'] = api_key

        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)

        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()
        print('Retrieved', len(data), 'characters')
        print(data.decode())
        tree = ET.fromstring(data)

        results = tree.findall('result')
        lat = results[0].find('geometry').find('location').find('lat').text
        lng = results[0].find('geometry').find('location').find('lng').text
        location = results[0].find('formatted_address').text

        print('lat', lat, 'lng', lng)
        print(location)

        add=tree.findall('result/address_component')
        check=False
        pos=0
        for info in add :
            for typ in info :
                if typ.text == 'country' :
                    check=True
                    break
            if check == True :
                break
            pos=pos+1

        if check == False :
            print('Country code not found')
            quit()

        code=add[pos].find('short_name').text
        print('Country Code:',code)
