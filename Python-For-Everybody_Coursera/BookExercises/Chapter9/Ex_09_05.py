fname=input('Enter a file name: ')
hnd=open(fname)
mail=dict()
for line in hnd :
    if not line.startswith('From:') :
        continue

    lst=line.split()
    word=lst[1]
    atpos=word.find('@')
    newwrd=word[atpos+1:]
    mail[newwrd]=mail.get(newwrd,0)+1

print(mail)
