import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser_addr = ('127.0.0.1', 12345)

while True:
		message = input('Enter a string to pass to Server and press "q" for quit.')
		message1 = message.encode()

		if message == 'q':
			break

		print('\n***********\nSending to Server {}'.format(message1))
		sent = s.sendto(message1, ser_addr)

		print('***********\nWaiting for Server message...')
		data, server = s.recvfrom(4096)

		print('***********\nReceived message from Server {}'.format(data))

		if data.decode() == 'q':
			print('\n***********\nClient is closing...')	
			print('***********\nClosing the socket...')
			break	

s.close()
