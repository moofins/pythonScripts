import sys
import socket
import argparse

def portInfo(ipAddress, port):	#there isn't any info back from non http ports i think, or its not as easy as just recv
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	resp = sock.recv(4096)
	print(resp)


def checkPort(ipAddress,port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#AF_INET means its ipv4 addresses, SOCK_STREAM means its 
																#TCP vs SOCK_DGRAM, which is UDP
	sock.settimeout(0.5)
	r = sock.connect_ex((ipAddress,port))
	if r == 0:
		return 1	#if its good, return a 1, if its bad, return 0
	else:
		return 0


def portScanner(ipAddress,ports):
	openPorts = []
	for port in ports:
		sys.stdout.flush()
		response = checkPort(ipAddress,port)
		if response == 1:
			#portInfo(ipAddress,port)	#there isn't any info back from non http ports i think, or its not as easy as just recv
			openPorts.append(port)
			sys.stdout.write("\033[K")  #clear line
			print(f"{ipAddress}:{port}")
		else:
			sys.stdout.write("\033[K")  #clear line
			print (f"[progress: {ipAddress}:{port}]", end='\r')
	return openPorts





def arguments():
    argList = [] #null list
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', required=True)
    #parser.add_argument('-p','--port')
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    argList = arguments()
    ipAddress = argList.url
    ports = range(1,65535)
    #if (argList.ports):
    #	ports = argList.ports
    #else:
    #	ports = range(1,65535)
    openPorts = portScanner(ipAddress, ports)
    if (openPorts):
    	print(f"Open ports are: {sorted(openPorts)}")
    else:
    	print("No ports found.")