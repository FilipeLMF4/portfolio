fname=input('Enter file: ')
hnd=open(fname)
lst=list()
for line in hnd :
    wds=line.split()
    for val in wds :
        if val in lst :
            continue
        lst.append(val)

lst.sort()
print(lst)
