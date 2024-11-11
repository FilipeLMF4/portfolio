fname = input('Enter the file name: ')

if fname == "na na boo boo" :
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()

try:
    hnd = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in hnd :
    if not line.startswith('Subject:') :
        continue
    count=count+1

print('There were', count, 'subject lines in', fname)
