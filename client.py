# Import socket module 
import socket			 

# Create a socket object 
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

# Define the port on which you want to connect 
port = 8080				

# connect to the server on local computer 
c.connect(('127.0.0.3', port)) 
# receive 4096 bytes data from the server 
print (c.recv(4096) )
# close the connection 
c.close()	 

