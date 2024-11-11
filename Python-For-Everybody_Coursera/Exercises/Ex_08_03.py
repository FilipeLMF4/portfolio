fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 :
        continue
    if len(words) < 2 or words[0] != 'From' :
        continue
    print(words[2])
