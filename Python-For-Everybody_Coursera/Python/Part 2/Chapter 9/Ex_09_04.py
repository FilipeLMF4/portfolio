name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

mail = dict()
lst = list()

#Creates list of addresses
for line in handle :
    if not line.startswith('From ') :
        continue
    lstx = line.split()
    lst.append(lstx[1])

#Creates dictionary with count of addresses
for ads in lst:
    mail[ads]=mail.get(ads,0)+1

#Creates histogram of address count
Mcount = None
Mkey = None
for ads,count in mail.items() :
    if Mcount is None or count > Mcount :
        Mkey = ads
        Mcount = count

print(Mkey,Mcount)
