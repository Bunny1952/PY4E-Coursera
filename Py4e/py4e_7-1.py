#py4e_7-1.py
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
	line = line.rstrip()
	new = line.upper()
	print (new)
