xfile = open('Chapter7.txt')
# print(xfile)

count = 0
for line in xfile :
    count = count + 1
    line = line.rstrip()
    print(line)

print ('Line Count:', count)


#r = xfile.read()
#print(r)
