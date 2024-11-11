def computegrade(xsc) :
    if xsc < 0 :
        return ("Bad Score")
    elif xsc < 0.6 :
        return ("F")
    elif isc <0.7 :
        return ("D")
    elif isc < 0.8 :
        return ("C")
    elif isc < 0.9 :
        return ("B")
    elif isc <= 1.0 :
        return ("A")
    else :
        return ("Bad Score")

score = input("Enter Score: ")
try:
    isc = float (score)
except:
    isc = -1

ssc=computegrade(isc)
print(ssc)
