hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
fhrs=float(hrs)
frate=float(rate)

if fhrs <= 40 :
    pay = fhrs*frate
else :
    pay=40*frate + (fhrs-40)*1.5*frate

print('Pay:', pay)
