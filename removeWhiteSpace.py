import sys

with open(sys.argv[1], "r+") as f:
	text = f.read()
	#text.replace(' ', '')
	#text.replace('\t','')
	#text.replace('\n','')	#join split works better than replace
	text = ''.join(text.split())
	f.seek(0)	#reset file cursor after read
	f.write(text)
	f.truncate()	#remove anything after written text, "hello" "write(bye)" would become "byelo" if no truncate