import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ser_addr = ('127.0.0.1', 12345)

print('\n***********\nStarting on {} port {}'.format(*ser_addr))
s.bind(ser_addr)

while True:
	print('***********\nWaiting for Client Message...')
	data, address = s.recvfrom(4096)

	print('***********\nReceived {} bytes from {}'.format(len(data), address))
	print(data)

	message = input('***********\nEnter a string to pass to Client ')
	message1 = message.encode()
	sent = s.sendto(message1, address)
	print('***********\nWe have sent {} bytes to {}'.format(sent, address))
