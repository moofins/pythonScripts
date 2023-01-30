import requests


target='http://loly.lc/wordpress/?attachment_id=' #parameter to fuzz
matchreq = requests.get('http://loly.lc/wordpress/?attachment_id=3') #page that should come up for every result
match=matchreq.text
for i in range(4,1000): #what range to use
	if (i == 12):
		continue
	url = target+str(i)
	r = requests.get(url)
	text = r.text
	if (text!=match):
		print(i)
		print(text)