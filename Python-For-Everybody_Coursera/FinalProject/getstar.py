import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
import time

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn=sqlite3.connect('starxml.sqlite')
cur=conn.cursor()

base_url='http://server2.sky-map.org'

cur.execute('''CREATE TABLE IF NOT EXISTS Stars_Raw
    (id INTEGER UNIQUE, url TEXT UNIQUE, xml TEXT)''')

#Pick up where we left off
cur.execute('SELECT max(id) FROM Stars_Raw' )
try:
    row = cur.fetchone()
    if row is None :
        starID = 0
    else :
        starID = row[0]
except:
    starID = 0

if starID == None :
    starID = 0

many = 0
count = 0
acount=0
badid=list()

while True :
    if many < 1 :
        sval=input('How many stars to import: ')
        if len(sval) < 1 :
            break
        try :
            many = int(sval)
        except:
            print('Invalid number.')
            continue

    if starID != 0 and acount == 0 :
        print('Restarting data extraction at star HD', starID)

    starID = starID + 1
    many = many - 1
    acount=acount+1

    surl = base_url + '/search?star=HD' + str(starID)

    #Check for valid information on URL
    try :
        uh = urllib.request.urlopen(surl, context=ctx)
        count = count + 1

    except KeyboardInterrupt :
        print('Process interrupted by user...')
        break

    except:
        if starID>359083 :
            print('=====End of Catalogue Reached. Quitting=====')
            print(len(badid), 'unretrieved stars in', acount)
            conn.commit()
            cur.close()
            quit()
        print('Unable to retrieve info on star HD', starID)
        badid.append(starID)
        cur.execute('''INSERT OR IGNORE INTO Stars_Raw(id,url,xml)
            VALUES (?,?,NULL)''', (starID,surl))
        continue

    data = uh.read().decode()
    #print(data)
    print('Star HD', starID, 'retrieved')

    cur.execute('''INSERT OR IGNORE INTO Stars_Raw(id,url,xml)
    VALUES (?,?,?)''', (starID,surl,data))

    if count % 50 == 0 : conn.commit()
    if count % 100 == 0 : time.sleep(5)

print(len(badid), 'unretrieved stars in', acount)
#print(badid)
conn.commit()
cur.close()
