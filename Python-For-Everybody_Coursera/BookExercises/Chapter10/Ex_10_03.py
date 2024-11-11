fname=input('Enter a file name: ')
hnd=open(fname)
lett=dict()
for line in hnd :
    line=line.rstrip()
    line=line.lower()
    for wds in line :
        if wds.isalpha() == False :
            continue
        lett[wds]=lett.get(wds,0)+1

lst=list()
for k, v in lett.items() :
    lst.append((v,k))

lst.sort(reverse=True)
for cnt, ltr in lst :
    print (ltr, cnt)
