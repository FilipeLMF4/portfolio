largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numf = int(num)
    except :
        print('Invalid input')
        continue

    if largest is None :
        largest = numf
        smallest = numf
    elif numf > largest :
        largest = numf
    elif numf < smallest :
        smallest = numf

print("Maximum is", largest)
print('Minimum is', smallest)
