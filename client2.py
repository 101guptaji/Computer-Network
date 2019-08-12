# Import socket module 
import socket			 

# Create a socket object 
c = socket.socket()		 

# Define the port on which you want to connect 
port = 8080				

# connect to the server on local computer 
c.connect(('127.0.0.3', port)) 
c.send(str.encode("client msg"))
# receive 4096 bytes data from the server 
print (c.recv(4096) )
# close the connection 
c.close()	 

