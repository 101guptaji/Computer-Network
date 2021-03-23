def ichecksum(data, sum=0):
    """ Compute the Internet Checksum of the supplied data.  The checksum is
    initialized to zero.  Place the return value in the checksum field of a
    packet.  When the packet is received, check the checksum, by passing
    in the checksum field of the packet and the data.  If the result is zero,
    then the checksum has not detected an error.
    """
    # make 16 bit words out of every two adjacent 8 bit words in the packet
    # and add them up
    for i in range(0,len(data),2):
        if i + 1 >= len(data):
            sum += data[i] & 0xFF
        else:
            w = ((data[i] << 8) & 0xFF00) + (data[i+1] & 0xFF)
            sum += w
    # take only 16 bits out of the 32 bit sum and add up the carries
    while (sum >> 16) > 0:
        sum = (sum & 0xFFFF) + (sum >> 16)

    # one's complement the result
    sum = ~sum

    return sum & 0xFFFF
#file = open('input4.txt', 'rb')
#data=file.read(512)
#print('data=',data)
#check=ichecksum(data)

#print(check)
#print(ichecksum(data,check))

