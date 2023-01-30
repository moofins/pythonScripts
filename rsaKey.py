

p = 7	#prime numbers
q = 11

n = p * q
phi = (p-1)*(q-1)	#the number of values less than n that are coprime to n.
eList = [] #values will need to be 2<e<phi, so as to be coprime to both n and phi and less than the value of phi
#^this is a list of possible PUBLIC keys, to be clear
for integer in range(2,phi):
	if (gcd(n,integer) == 1 and gcd(phi,integer == 1)):	#if the gcd of both are 1, they're coprime to both nums
		eList.append(integer)

dList = []
e = eList[0]	#just using a value for e as an example
#^this is a list of possible PRIVATE keys
for integer in range(phi+1, phi+1000):	#just needs to be some amount greater than phi, 1000 is picked arbitrarily
	if (integer * e % phi == 1):
		dList.append(integer)

#in our example, n = 37627, e = 23, d = 61527