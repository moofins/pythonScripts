import requests
import argparse
import sys
import asyncio
import aiohttp
from colorama import Fore


async def HTTPpost(session, url,passwords,username,formatting,failtext,progress):

	#response = sendHTTPPost(url, password, username, formatting)
	data = formatting.replace('^USER^',username).replace('^PASS^',password)	#python being friendly with making this easy
	print(f"http POSTING! {data}", end='\r')
	#sys.stdout.write("\033[K")  #clear line
	#print(Fore.WHITE + f"[progress: {progress}] | {username}:{password}", end='\r')	
	async with session.post(url,data=data) as r:
		print(r.status)
		#if (response.find(failtext) == -1):	#if we don't find the fail text, we found a valid login!
		#	sys.stdout.write("\033[K")  #clear line
		#	print(Fore.GREEN + f"Login found: {formatting.replace('^USER^',username).replace('^PASS^',password)}", end='\n')

async def fuzzASYNC(url,passwords,username,formatting,failtext):
	progress = 0
	async with aiohttp.ClientSession() as session:
		tasks = []
		for password in passwords.readlines():
			password = password.strip()
			progress += 1
			task = asyncio.ensure_future(HTTPpost(session, url, password, username, formatting, failtext, progress))
			tasks.append(task)
		await asyncio.gather(*tasks, return_exceptions=True)
			


def fuzzPasswords(url, passFile, username, formatting, failtext):
	with open(passFile, 'r', encoding='latin-1') as passwords:
		asyncio.get_event_loop().run_until_complete(fuzzASYNC(url,passwords,username,formatting,failtext))
		

def arguments():    #parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', required=True)
    parser.add_argument('-p','--passwords', required=True)
    parser.add_argument('-l','--username', required=True)
    parser.add_argument('-f','--format', required=True)
    parser.add_argument('-a','--failure', required=True)
    args = parser.parse_args()

    return args

if __name__ == "__main__":
	argList = arguments()
	with open(argList.passwords, 'r', encoding='latin-1') as passwords:
		asyncio.get_event_loop().run_until_complete(fuzzASYNC(argList.url,passwords,argList.username,argList.format,argList.failure))