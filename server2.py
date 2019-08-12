import socket			 
from _thread import *
# next create a socket object 
s = socket.socket()	
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 8080 but it can be anything 
port = 8080			

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes listen to requests 
# coming from other computers on the network 
ip=''

try:
	s.bind((ip, port))		 
	print ("socket binded to %s" %(port) )
except socket.error as e:
	print(str(e))

# put the socket into listening mode 
s.listen(1)
print ("socket is listening")		
def threaded_client(conn):
	conn.send(str.encode("server msg\n"))
	print(conn.recv(4096))
	conn.close()

# a forever loop until we interrupt it or 
# an error occurs 
while True: 
	# Establish connection with client. 
	conn,addr = s.accept()	 
	print ('Got connection from' +addr[0]+': '+ str(addr[1]))
	start_new_thread(threaded_client,(conn,))
