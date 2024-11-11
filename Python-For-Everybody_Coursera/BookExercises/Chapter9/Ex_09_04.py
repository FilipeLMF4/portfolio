fname=input('Enter a file name: ')
hnd=open(fname)
mail=dict()
for line in hnd :
    if not line.startswith('From ') :
        continue

    lst=line.split()
    word=lst[1]
    mail[word]=mail.get(word,0)+1

largest = 0
for k,v in mail.items() :
    if v > largest :
        largest = v
        largName = k
                
print(largName, largest)
