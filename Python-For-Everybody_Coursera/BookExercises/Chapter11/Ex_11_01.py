import re

regex = input('Enter Regular Expression: ')
file = input('Enter file name: ')
hnd=open(file)
count = 0

for line in hnd :
    lst = re.findall(regex, line)
    if len(lst) == 0 :
        continue
    count=count + 1

print (file,'had',count,'lines that matched',regex)
