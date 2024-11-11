str = 'X-DSPAM-Confidence:0.8475'
pos=str.find(':')
val=str[pos+1:]
fval=float(val)
print(fval)
