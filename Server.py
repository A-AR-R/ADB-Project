import SocketServer
from storage import Storage
from HomomorphicAlgorithm import ValidateHomomorphicEncryption
storage=Storage()
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print "{} requested cipher : ".format(self.client_address[0]),self.data
                rcipher=self.data.split(",")
                for cipher in storage.keywords:
                    v = ValidateHomomorphicEncryption(cipher[0], (int(rcipher[0]), int(rcipher[1])), (cipher[1], cipher[2]))
                    v.XorFirstHalves()
                    if v.XorSecondHalves() == v.CalulateSecondHalvesWithHomomorphicFeature():
                        self.request.sendall("matched")
                    else:
                        pass
                self.request.sendall("not matched")
            except:
                break



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()