import requests
import sys
import pathlib
from colorama import Fore, Style

#print all comments in pages, to check for easy pwns, if you will

#url = sys.argv[1] #argument was url, now take from directory listing output by dirfuzz.py

def findComments(content):
	i = 0
	while (i < len(content)):	#until the end of the response
		startComment = content.find('<!',i)	#could make an option for which type to find, for now its just "<!comments>"
		endComment = content.find('>',startComment) + 1
		if (startComment != -1):	#if fail to find, that's the end of the doc
			print(Fore.YELLOW + Style.DIM + content[startComment:endComment])
			i = endComment
		else:
			i = len(content)

def findKeyWords(content):
	keywords = ["password", "Password", "pwd", "passwd", "user", "username", "Username", "uname", "id:", "ID:"]	#a couple of sus words
	for word in keywords:
		wordLocation = content.find(word)
		if (wordLocation != -1):
			print(Fore.BLUE + Style.NORMAL + f"Keyword found! [{word}]")
		else:
			continue

with open(pathlib.Path(__file__).parent / 'curDirList.txt','r',encoding='latin-1') as dirFile:
	for urlLine in dirFile.readlines():
		url = urlLine[8:urlLine.find('\n')]
		print(Fore.WHITE + Style.NORMAL + url)
		try:
			r = requests.get(url)
			if (r.status_code != 200):
				raise Exception(Fore.RED + Style.DIM + "Not 200 code.")
			else:
				content = r.content.decode()
				findComments(content)
				findKeyWords(content)
		except Exception as e:
			print(e)
			#exit(0)	#dont exit on exception, as i still wanna see the other pages in this updated version
