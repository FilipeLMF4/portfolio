import re
name = input('Enter file: ')
hnd=open(name)
sum=0
#count=0

for line in hnd :
    lst=re.findall('[0-9]+', line)
    if len(lst) == 0 :
        continue
    for num in lst :
        flt=float(num)
        #count=count+1
        sum=sum+flt

#print(count)
print (sum)
