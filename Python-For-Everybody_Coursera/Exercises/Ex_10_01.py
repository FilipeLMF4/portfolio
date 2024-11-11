fname=input('Enter a file name: ')
hnd=open(fname)
mail=dict()
for line in hnd :
    if not line.startswith('From ') :
        continue

    lst=line.split()
    word=lst[1]
    mail[word]=mail.get(word,0)+1
lst=list()
for k, v in mail.items() :
    lst.append((v, k))

lst.sort(reverse=True)
count, mail=lst[0]

print (mail, count)
