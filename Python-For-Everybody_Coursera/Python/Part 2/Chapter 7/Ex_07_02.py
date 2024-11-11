# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
newval = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    val = line.find(':')
    valstr = line[val+1:]
    valf=float(valstr)
    newval = newval + valf

avg = newval/count

print("Average spam confidence:", avg)
