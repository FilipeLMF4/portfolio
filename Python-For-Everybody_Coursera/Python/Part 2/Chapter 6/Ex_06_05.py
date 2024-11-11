text = "X-DSPAM-Confidence:    0.8475"
beg =text.find('0')
numb = text[beg:]
print(float(numb))
