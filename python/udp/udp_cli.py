#UDP server
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',12345))
msg, addr = s.recvfrom(1024)
msg = msg.decode().upper()
s.sendto(msg.encode()   ,addr)
s.close()