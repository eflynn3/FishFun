from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall
from game import GameSpace

START_PORT = 40111
GAME_PORT = 40126

playGame = GameSpace()

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

class GameConnection(Protocol):
    def connectionMade(self):
        print "Created game connection"
        playGame.main("1", self)
        gameLoop = LoopingCall(playGame.gameLoop)
        gameLoop.start(0.0166)

        dataLoop = LoopingCall(self.getData)
        dataLoop.start(0.5)

    def dataReceived(self, data):
    	print data
        playGame.updateFish2(data)


    def getData(self):
        playGame.getData()

class GameFactory(ClientFactory):
    def __init__(self):
    	self.myConn = GameConnection()

    def buildProtocol(self, addr):
    	return self.myConn

if __name__ == '__main__':

	reactor.listenTCP(START_PORT, StartFactory())

	reactor.run()