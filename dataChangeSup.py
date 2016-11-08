#    path : cd C:\users\user\Desktop(in my home)
#    permission => admistrator (we need admin permission)
#
#    마이클 => [235, 167, 136, 236, 157, 180, 237, 129, 180]
#    it means
#    >>> a=마이클
#    >>> b=a.encode()
#    >>> c=list(b)

#    Michael => [77, 105, 99, 104, 97, 101, 108] used for findMichael
#    it means
#    a=Michael
#    b=a.encode()
#    c=list(b)

#    GILBERT => [71, 73, 76, 66, 69, 82, 84] used for data change
#    it means
#    >>> a=GILBERT
#    >>> b=a.encode()
#    >>> c=list(b)


def listPrint(a) : #function for test
    for k in a :
        print(chr(k), end='')

# findGzip is used for...
# input : listed(bytes object)
# result : find list factor which means 'Gzip,' and change to '     '(5 spaces)
def findGzip(a) : #type(a) is expected to be list
    listSize = len(a)
    for i in range(listSize-4) :
        if(chr(a[i]) == 'g' and chr(a[i+1]) == 'z' and chr(a[i+2]) == 'i' and chr(a[i+3]) == 'p' and chr(a[i+4]) == ',') :
            a[i] = ord(' ') #32 == ord(' '), means space
            a[i+1] = ord(' ')
            a[i+2] = ord(' ')
            a[i+3] = ord(' ')
            a[i+4] = ord(' ')
            break

# principle of findMichael is similar to findGzip
# input : listed(bytes object)
# result : find list factor which means 'Michael' and change to 'GILBERT'
def findMichael(a) : #type(a) is expected to be list
    listSize = len(a)
    for i in range(listSize-6) :
        if(chr(a[i]) == 'M' and chr(a[i+1]) == 'i' and chr(a[i+2]) == 'c' and chr(a[i+3]) == 'h' and chr(a[i+4]) == 'a' and chr(a[i+5]) == 'e' and chr(a[i+6]) == 'l') :
            a[i] = ord('G') #32 == ord(' '), means space
            a[i+1] = ord('I')
            a[i+2] = ord('L')
            a[i+3] = ord('B')
            a[i+4] = ord('E')
            a[i+5] = ord('R')
            a[i+6] = ord('T')
            break

#pydivert is python-implemented Windivert
import pydivert

#for capture only http
w = pydivert.WinDivert("(tcp.DstPort == 80) or (tcp.SrcPort == 80) and (tcp.PayloadLength > 0)")

#open session
w.open()

#packet capture, manipulation, and resend to L3
while(1) :
    # capture 1 packet
    packet = w.recv()

    # decide whether packet is in-path(inbound) or out-path(outbound)
    # if packet is out-path
    if(packet.is_outbound == True) :
        tempList = list(packet.payload)
        findGzip(tempList)  # DataChange in outbound : replace 'gzip,' with '     '
        changedPayload = bytes(tempList)
        packet.payload = changedPayload
        print(packet)
        w.send(packet)
    # if packet is in-path
    if(packet.is_inbound == True):
        tempList = list(packet.payload)
        findMichael(tempList)  # DataChange in inbound : replace 'Michael' with 'GILBERT'
        changedPayload = bytes(tempList)
        packet.payload = changedPayload
        print(packet.payload)
        w.send(packet)

# In reality, because of infinite loop above, this line will not be read
w.close()



