from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor 
from twisted.internet.defer import DeferredQueue
from game import GameSpace

START_PORT = 40111
GAME_PORT = 40126

playGame = GameSpace()

class GameConnection(Protocol):
    def connectionMade(self):
        print "Created game connection"
        playGame.main("1")
    def dataReceived(self, data):
    	print "data received"

class GameFactory(ClientFactory):
    def __init__(self):
    	self.myConn = GameConnection()

    def buildProtocol(self, addr):
    	return self.myConn


# initial connection for listening for a client, before beginning game connection
# (perhaps unnecessary and redundant)
class StartConnection(Protocol):
    def connectionMade(self):
        print "Other player joined..."
        self.transport.write("start")
        reactor.listenTCP(GAME_PORT, GameFactory()) # Initial connection made to 
    def dataReceived(self, data):
        pass

class StartFactory(ClientFactory):
    def __init__(self):
    	self.myConn = StartConnection()

    def buildProtocol(self, addr):
    	return self.myConn

##################################

if __name__ == '__main__':

	reactor.listenTCP(START_PORT, StartFactory())

	reactor.run()