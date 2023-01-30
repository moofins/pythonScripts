import pickle

f = open('/home/kali/pythontesting/credspickle.dat', "rb")
f.seek(0)

data = pickle.load(f)
print(data)

sshuserlen=6
sshpasslen=27

sshUser=[]
for i in range(7):
	sshUser.append(i)
sshPass=[]
for i in range(28):
	sshPass.append(i)
	
for entry in data:
	if (entry[0].find('ssh_pass') != -1):	#if it is ssh_pass
		letterPlace=int(entry[0][8:])
		sshPass[letterPlace]=entry[1]
	else:
		letterPlace=int(entry[0][8:])
		sshUser[letterPlace]=entry[1]
	#print(f"{sshUser}: {sshPass}", end='\r')
sshUserString = ""
for char in sshUser:
	sshUserString+=char
sshPassString = ""
for char in sshPass:
	sshPassString+=char
print(f"{sshUserString}: {sshPassString}")

