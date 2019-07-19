# Code using a dictionary to count the number of From lines in a list
# counting the 2nd word, which is an email address in a lit of emails.
#The program will find the emaild address that has the most From messages.


name = input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

#Create the dictionary and read the file line by line into
#a list of words.
counts = dict()
for line in handle:
	if not line.startswith("From ") : continue
	words = line.split()
#	print(words)
	words = words[1]
#	print(words)
#This part makes the histogram of the words in the list.
#	for word in words:
	counts[words] = counts.get(words, 0) + 1
#	print('Counts', counts)
#Search for the word with the highest value from the 
#items which are the key-value pairs.
bigcount = None
bigword = None
for word,count in counts.items() :
	if bigcount is None or count > bigcount :
		bigword = word
		bigcount = count


print(bigword, bigcount)