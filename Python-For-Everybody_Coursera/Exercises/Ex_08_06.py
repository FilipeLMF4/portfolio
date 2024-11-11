lst=list()
while True :
    nmb = input('Enter a number: ')
    if nmb == "done" :
        break
    try :
        fnmb = float(nmb)
    except :
        print('Invalid Input')
        continue

    lst.append(fnmb)


print('Maximum:', max(lst))
print('Minimum:', min(lst))
