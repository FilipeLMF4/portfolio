fname=input('Enter a file name: ')
hnd=open(fname)
mail=dict()
for line in hnd :
    if not line.startswith('From ') :
        continue

    val=line.find(':')
    hr=line[val-2:val]
    mail[hr]=mail.get(hr,0)+1

lst=list()
for k, v in mail.items() :
    lst.append((k,v))

lst.sort()
for hr, x in lst :
    print(hr, x)
