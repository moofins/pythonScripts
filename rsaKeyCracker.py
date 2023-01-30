#in our example, n = 37627, e = 23, d = 61527
import sys
n = 37627
e = 23
d = 61527


with open("rsakeyfile.txt","r") as key:
	for line in key:
		for word in line.split():
			asciiChar = int(word) ** d % n
			character = chr(asciiChar)
			sys.stdout.write(character)