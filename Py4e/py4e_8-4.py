

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
final = list()
x = 0
i = 0
for line in fh:
	stuff = line.split()
	x = 0
	for i in stuff:
		lst.append(stuff[x])
		x = x + 1
lst.sort()	#The list lst is sorted.
#Now look for duplicates and remove them.
#x = 0
#i = 0
#for z in lst:
for i in range(len(lst)):
#print(stuff)
	#i = len(stuff)
	while lst[i] not in final:
	#print(lst[i])
		final.append(lst[i])
		#continue
print(final)
#Code above works. It creates 1 list lst
#to be sorted and remove the duplicates.

#print(line.rstrip())
#for i in range(len(stuff))
#print(stuff)
	#i = len(stuff)
#i = i - 1
	#print(i)
	#word = stuff(i)