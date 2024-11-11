# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
doc = fh.read()
docU = doc.upper()
print(docU.rstrip())
