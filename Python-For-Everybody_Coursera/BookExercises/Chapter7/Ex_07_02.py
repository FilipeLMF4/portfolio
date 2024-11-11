fname = input('Enter the file name: ')
if fname == "" :
    fname = 'mbox-short.txt'

hnd = open(fname)
count = 0
total = 0
for line in hnd :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    line=line.rstrip()
    pos=line.find(':')
    val=line[pos+1:]
    fval=float(val)
    total=total+fval
    count=count+1

print('Average spam confidence:', total/count)
