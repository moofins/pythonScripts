import sys
import os

programfilesFile=sys.argv[1]

searchlist=[]

skiplist=['.','..','Common Files','Windows Defender','Windows Mail','Windows Media Player','Windows Multimedia Platform','Windows NT','Windows Photo Viewer','Windows Portable Devices','WindowsPowerShell','Internet Explorer','Microsoft.NET','Windows Security','Windows Defender Advanced Threat Protection','VMware','ModifiableWindowsApps']

with open(programfilesFile, 'r', encoding='latin-1') as f:
	for line in f.readlines():
		start=line.find("<DIR>")+15
		program = line.strip()[start:]
		if ():	#remove directory notation from the search as that'll bust things.
			continue
		else:
			searchlist.append(program)

for bad in skiplist:
	for program in searchlist:
		if (program == bad):
			searchlist.remove(bad)

for program in searchlist:
	print("\t\t"+program+"\t\t")
	os.system(f"searchsploit {program}")