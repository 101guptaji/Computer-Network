import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

port = 12345

s.connect(('127.0.0.1', port))

while True:
    message = input('Enter numbers for operations or enter q to quit connetion: ')
    message1 = message.encode()
    s.send(message1)
    if message == 'q':
        break
    message2 = input('Enter numbers for operations or enter q to quit connetion: ')
    message3 = message2.encode()
    s.send(message3)
    if message2 == 'q':
        break
    ser_add_msg = s.recv(4096).decode()
    ser_sub_msg = s.recv(4096).decode()
    print('Message from Server - Addition: ',ser_add_msg)
    print('Message from Server - Subtraction: ',ser_sub_msg)

s.close()

