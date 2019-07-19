
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = 0 #counter
b = 0.0 #text as a number using float
c = 0.0 #average
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    nline = line[20:26]
    b = float(nline)
    c = c + b
    a = a + 1
c = c / a
print('Average spam confidence:', c)

#Average spam confidence: 0.750718518519
