import socket
from _thread import *
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8086))
def send(s):
	while True:
		message=input()
		s.send(message.encode())
		if not message:
			break
			exit()
def recv(s):
	while True:
		message1=s.recv(1096)
		if not message1:
			break
			s.close()
			client.close()
		else:
			print("\n***********\nServer - ", message1.decode())

thread1=threading.Thread(target=send, args=(client,))
thread2=threading.Thread(target=recv, args=(client,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
client.close()
