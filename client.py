from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor 
from game import GameSpace
import sys

START_PORT = 40111
GAME_PORT = 40126
HOST = ""
class StartConnection(Protocol):
    def connectionMade(self):
		print "client connection made"        
    def dataReceived(self, data):
        if(data == "start"):
            reactor.connectTCP(HOST, GAME_PORT, GameFactory())
        print "client data received"

class StartFactory(ClientFactory):
    def __init__(self):
    	self.myConn = StartConnection()

    def buildProtocol(self, addr):
    	return self.myConn    

    def startedConnecting(self, connector):
        print "Began Initial Connection"

    def clientConnectionLost(self, connector, reason):
        print "ERROR: Lost initial connection\n", reason
    def clientConnectionFailed(self, connector, reason):
        print "ERROR: Could not establish initial connection\n", reason

class GameConnection(Protocol):
    def connectionMade(self):
        print "connected to game host"

    def dataReceived(self, data):
       #game.get_remote(data)
       print "client game received"

class GameFactory(ClientFactory):
    def __init__(self):
    	self.myConn = GameConnection()

    def buildProtocol(self, addr):
    	return self.myConn

    def startedConnecting(self, connector):
        print "Began game connection with host"
    def clientConnectionLost(self, connector, reason):
        print "ERROR: Lost Connection\n", reason
    def clientConnectionFailed(self, connector, reason):
        print "ERROR: Connection Failed\n", reason

if __name__ == '__main__':
    HOST = sys.argv[1]
    reactor.connectTCP(HOST, START_PORT, StartFactory())

    reactor.run()
