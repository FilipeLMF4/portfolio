name = input("Enter file:")

if len(name) < 1 :
    name = "mbox-short.txt"

handle = open(name)
di=dict()
lst = list()

for line in handle :
    if not line.startswith('From ') :
        continue

    val=line.find(':')
    line=line[(val-2):(val)]
    di[line]=di.get(line,0)+1

for k,v in di.items() :
    lst.append((k,v))

lst=sorted(lst)
for hr,x in lst :
    print(hr, x)
