hrs = input('Enter Hours: ')
try:
    fhrs=float(hrs)
except:
    print('Error, please enter numeric input')
    quit()

rate = input('Enter Rate: ')

try:
    frate=float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if fhrs <= 40 :
    pay = fhrs*frate
else :
    pay=40*frate + (fhrs-40)*1.5*frate

print('Pay:', pay)
