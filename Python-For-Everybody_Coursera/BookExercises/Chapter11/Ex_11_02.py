import re

file = input('Enter file: ')
hnd = open(file)

count=0
sum=0

for line in hnd :
    lst = re.findall('New Revision: ([0-9]+)',line)
    if len(lst) == 0 :
        continue
        
    for num in lst :
        count = count + 1
        numf = float(num)
        sum = sum + numf

avg = sum/count
avg=int(avg)

print(avg)
