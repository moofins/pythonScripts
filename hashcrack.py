import bcrypt
import base64
import sys

salt=b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.'
hashandsalt=b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.3h9WhI/A0Rcbchmvk10KWRMWe4me81e'

file = sys.argv[1]
i = 0
with open(file, "r", errors='ignore') as f:
	print("rockyou opened")
	firsttime=True
	for passw in f.readlines():
		if (firsttime):
			print("f.readlines() passed")
			firsttime=False
		i = i+1
		passw = passw.strip().encode('ascii', 'ignore')
		b64str = base64.b64encode(passw)
		hashtest=bcrypt.hashpw(b64str, salt)
		if (bcrypt.checkpw(hashtest, hashandsalt)):
			print(f"\nPass found: {passw}")
			exit(0)
		else:
			print(f"testing: {i}")