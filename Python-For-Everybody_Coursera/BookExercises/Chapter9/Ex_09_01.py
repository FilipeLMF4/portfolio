hnd=open('words.txt')
dct=dict()
lst=list()
for line in hnd :
    wds=line.split()
    for val in wds :
        dct[val]='y'

word = input('Enter word: ')
if word in dct :
    print(word, 'is in the dictionary')
else :
    print(word, 'is not in the dictionary')
