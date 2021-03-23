import socket
from _thread import *
import threading


server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8086))
server.listen(10)

def recv(con):
	while True:
		message=con.recv(1096)
		if not message:
			break
		else:
        		print("\n***********\nClient - ",message.decode())

def Send(con):
	while True:
		send_input=input()
		con.send(send_input.encode())
		if not send_input:
			con.close()           
			#thread2.join()
			#thread1.join()

def New_Connection(connection):
	thread1=threading.Thread(target=recv, args=(connection,))
	thread2=threading.Thread(target=Send, args=(connection,))
	thread1.start()
	thread2.start()
	thread2.join()
	thread1.join()

while True:
    	connection, addr = server.accept()
    	print("\n***********\nConnection is established")
    	New_Connection(connection)


