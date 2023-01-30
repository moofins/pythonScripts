import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
mess = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#DGRAM is UDP connection
messByte = mess.encode()	#can only send bytes
sock.sendto(messByte, (ip, port))
r = sock.recv(4096)
print(r.decode())