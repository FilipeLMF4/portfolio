def computepay(xhrs,xrate) :
    if xhrs <= 40 :
        pay = xhrs*xrate
    else :
        pay=40*xrate + (xhrs-40)*1.5*xrate

    print('Pay:', pay)

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

computepay(fhrs,frate)
