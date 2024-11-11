fname = input('Enter a file name: ')
hnd=open(fname)
count=0
for line in hnd :
    if not line.startswith('From ') :
        continue

    lst=line.split()
    count=count+1
    print(lst[1])

print('There were',count,'lines in the file with From as the first word')
