#UDP client

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("Hello".encode(),('localhost',12345))
msg, addr = s.recvfrom(1024)
print("Server says : ",msg.decode())
s.close()