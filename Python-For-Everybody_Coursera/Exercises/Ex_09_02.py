fname=input('Enter a file name: ')
hnd=open(fname)
mail=dict()
for line in hnd :
    if not line.startswith('From ') :
        continue

    lst=line.split()
    word=lst[2]
    mail[word]=mail.get(word,0)+1

print(mail)
