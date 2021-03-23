import socket
from _thread import *               
import threading 


def client(c_socket,address):
	while True:
		message1 = c_socket.recv(1024).decode()
		if message1 == 'q':
			break
		message1 = int(message1)
		print("data1=",message1)
		message3 = c_socket.recv(1024).decode()
		if message3 == 'q':
			break
		message3 = int(message3)
		print("data2=",message3)
		ser_add_msg = message1 + message3
		ser_sub_msg = message1 - message3
		ser_add_msg = str(ser_add_msg)
		ser_sub_msg = str(ser_sub_msg)
		c_socket.send(ser_add_msg.encode())
		c_socket.send(ser_sub_msg.encode())
	c_socket.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)         
 
port = 12345               
print ('Server has started...')
print ('Waiting for clients...')

s.bind(('127.0.0.1', port))        
s.listen(10)                 

while True:
	c, address = s.accept()
	print ('Got connection from', address)
	t=threading.Thread(target=client,args=(c,address))
	t.start()
	
s.close()

