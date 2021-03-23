# packet.py - Packet-related functions
from checksum import *
# Creates a packet from a sequence number,byte data and checksum
def make(seqnum, data = b''):
	seqbytes = seqnum.to_bytes(4, byteorder = 'little', signed = True)
	#print('data=',data)
	check = ichecksum(data)
	print('check=', check)
	checkb=check.to_bytes(3, byteorder = 'big', signed = True)
	print('checkb=', checkb)
	return seqbytes + data + checkb

# Creates an empty packet
def make_empty():
    return b''

# Extracts sequence number and data from a non-empty packet
def extract(packet):
	seqnum = int.from_bytes(packet[0:4], byteorder = 'little', signed = True)
	check=packet[-3:-1]
	data=packet[4:]
	result=ichecksum(data,check)
	if(result==0):
		return seqnum, packet[4:]
	else:
		print("error in data")
