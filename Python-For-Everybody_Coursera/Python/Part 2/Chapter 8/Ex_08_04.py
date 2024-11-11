fname = input("Enter file name: ")
fh = open(fname)
lstx = list()
lst = list()
for line in fh:
    lstx = line.split()
    for words in lstx :
        if words not in lst:
            lst.append(words)

lst.sort()
print(lst)
