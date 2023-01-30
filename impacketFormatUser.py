import sys

file = sys.argv[1]
namelist=[]

with open(file, "r+") as f:
	lines = f.readlines()
	for line in lines:
		if (line.find("(SidTypeUser)") != -1):	#if it is found, ie, not -1
			startName = line.find("\\") + 1 #+1 so we're one past the found char
			endName = line.find(" ",startName)
			name = line[startName:endName]
			namelist.append(name)
			#print(name)

	f.seek(0)
	for name in namelist:	#for each valid user name, write back to the file
		f.write(name + '\n')
	f.truncate()
