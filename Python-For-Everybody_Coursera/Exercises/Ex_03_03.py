score = input("Enter Score: ")
try:
    isc = float (score)
except:
    isc = -1
if isc < 0 :
    print ("Invalid score (not a number)")
elif isc < 0.6 :
    print ("F")
elif isc <0.7 :
    print ("D")
elif isc < 0.8 :
    print ("C")
elif isc < 0.9 :
    print ("B")
elif isc <= 1.0 :
    print ("A")
else :
    print ("Invalid score (>1)")
