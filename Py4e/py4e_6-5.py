

text = "X-DSPAM-Confidence:    0.8475";
apos = text.find('0')
print(apos)
epos = text.find('5')
print(epos)
x = data[apos : epos]
y = float(x)
print(y)
