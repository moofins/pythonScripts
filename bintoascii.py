import sys
#binary = bin(int(sys.argv[1]))
#print(binary)
#print(type(binary))
f = open(sys.argv[1], "r")
binary = f.read()
f.close()
binary = binary.replace(' ','')

length = int(len(binary)/8)
#print(f"Length: [{length}]\n")

for letter in range(length):
	start = letter*8
	letterBin = binary[start:start+8]
	letterInt = int(letterBin,2)
	print(chr(letterInt), end="")