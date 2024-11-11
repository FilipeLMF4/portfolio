def computepay (h,r) :
    hf = float(h)
    rf = float(r)
    if hf <=40  :
        pay = hf*rf
    else :
        pay = 40 * rf + (hf-40) *1.5 * rf
    return pay

hrs = input ("Enter Hours:")
rate = input ("Rate of Pay:")

p = computepay(hrs,rate)
print ("Pay", p)
