import sys

file = sys.argv[1]
listWords=[]

with open(file, "r+") as f:
	lines = f.readlines()
	for word in lines:
		wordLow=word.lower()
		wordUpp=word.upper()
		wordCap=word[0].upper()+word[1:]
		listWords.append(wordLow.strip())
		listWords.append(wordUpp.strip())
		listWords.append(wordCap.strip())

	f.seek(0)
	for word in listWords:	#for each valid user name, write back to the file
		f.write(word + '\n')
	f.truncate()
