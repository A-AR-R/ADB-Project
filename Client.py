import socket
from HomomorphicAlgorithm import HomomorphicEncryption
from datetime import datetime
HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        keyword = raw_input("input: ")
        if len(keyword)<3:
            print "keyword too short!"
            continue
        if keyword=="quit":
            break
        encrypt_keyword = HomomorphicEncryption()
        encrypt_keyword.set_text(keyword.strip(), datetime.now())
        sio2 = encrypt_keyword.get_sio_2()
        cioL = encrypt_keyword.get_cioL()
        pad2 = encrypt_keyword.get_fkio()
        cioR = encrypt_keyword.get_cioR()

        sock.send(str(cioL)+","+str(cioR))
        received = sock.recv(1024)
        print "received : ",received
finally:
    sock.close()