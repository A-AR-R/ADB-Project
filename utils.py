__author__ = 'Alipour'

def split_string(string):
    temp=[]
    for i in string:
        temp.append(i)
    return temp

def char2bin(character):
    data=bin(ord(character))[2:]
    for i in range(8-len(data)):
        data="0"+data
    return data
def bin2char(binary):
    return chr(int(binary,2))

def string2bin(string):
    pad=""
    for i in string:
        pad+=char2bin(i)
    return pad
def bin2string(pad):
    data=""
    for i in range(0,len(pad),8):
        data+=chr(int(pad[i:i+8],2))
    return data
def string2integer(string):
    return int(string2bin(string),2)
def addpadd(binary):
    data=binary
    while len(data)%8!=0:
        data="0"+data
    return data
def integer2string(integer):
    return bin2string(addpadd(format(integer,'b')))
