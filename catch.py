import socket
import sys
import time

startPort = 1337	#1337 is the start of the chain
host = sys.argv[1]

firstScreen = True
failures = 0

port = startPort

def mathOperate(response, value):
	endHeaderLocation = response.decode().find('GMT\r\n\r\n') + 7
	endHeader = response.decode()[endHeaderLocation:len(response)]
	print(endHeader)
	firstSpace = endHeader.find(' ')
	secondSpace = endHeader.find(' ', firstSpace+1)	#+1 bc firstSpace is the location of the space, so otherwise second=first

	op = endHeader[0:firstSpace]
	opValue = endHeader[firstSpace+1:secondSpace]
	nextPort = endHeader[secondSpace+1:len(endHeader)]	#seems like len returns the correct length, not 1 more than? idk, annoying

	value = operator(op, float(opValue), value)
	print(f"Current value is: {value}")

	return (int(nextPort), value)

def operator(op, opValue, value):
	if (op == "add"):
		value = value + opValue
	elif (op == "minus"):
		value = value - opValue
	elif (op == "multiply"):
		value = value * opValue
	elif (op == "divide"):
		value = value / opValue
	return value

if __name__ == "__main__":
	value = 0.0
	while(port != 9765):	#loop until end condition met
		try:	#make socket
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print("socket failed!")
			exit(0)
		sys.stdout.write("\033[K")
		print(f"trying {host}:{port}...")
		connect = False
		while (connect == False):
			try:
				client.connect((host,port))	#try to connect until port is up
				connect = True
			except socket.error:
				failures += 1
				sys.stdout.write("\033[K")
				print(f"Connection was refused! retrying... [{failures}]", end = '\r')
				time.sleep(3)
				continue

		sys.stdout.write("\033[K")
		failures = 0	#clear and reset after success


		request = f"GET / HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n"	#http needs to be formatted with \r\n (CR LF) after lines and one blank at end
		client.sendall(request.encode())
		time.sleep(3)	#slow down code so we don't reconnect to port while already connected

		response = client.recv(4096)
		httpResponse = repr(response)
		print(response)
		port, value = mathOperate(response, value)	#returning tuple bc it couldn't identify global variable value. probably better way