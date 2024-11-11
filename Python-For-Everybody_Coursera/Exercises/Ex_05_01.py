total = 0
count = 0

while True :
    nmb = input('Enter a number: ')
    if nmb == "done" :
        break
    try :
        fnmb = float(nmb)
    except :
        print('Invalid Input')
        continue

    total=total + fnmb
    count=count + 1

print(total, count, total/count)
