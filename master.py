#Programming paradigms 
#Master.py to create starting connection and game connection
#Erin Flynn and Erin Turley

from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall
from game import GameSpace

START_PORT = 40111 #port for opening connection 
GAME_PORT = 40126 #port for game connection 

playGame = GameSpace() #instantiate gamespace for player 1

# Start opening connectction 
class StartConnection(Protocol):
    def connectionMade(self):
        print "Other player joined..."
        self.transport.write("start") #once player has joined, write start to initialize game
        reactor.listenTCP(GAME_PORT, GameFactory()) # Initial connection made to game port 
    
    def dataReceived(self, data):
        pass

class StartFactory(ClientFactory):
    def __init__(self):
        self.myConn = StartConnection()

    def buildProtocol(self, addr):
        return self.myConn

#Start connection to play the game 
class GameConnection(Protocol):
    def connectionMade(self):
        #loopingCall reference: http://www.saltycrane.com/blog/2008/10/running-functions-periodically-using-twisteds-loopingcall/
        playGame.main("1", self) #instantiate player 1 gamespace
        gameLoop = LoopingCall(playGame.gameLoop) #begin iteration of loop (like clock tick(60))
        gameLoop.start(0.0166) #tick 1/60

        dataLoop = LoopingCall(self.getData) #loop for sending data
        dataLoop.start(0.5) #send data ever half second

    def dataReceived(self, data):
        playGame.updateFish2(data) #process the data received from player 2


    def getData(self):
        playGame.getData() #send the data to player 1

class GameFactory(ClientFactory):
    def __init__(self):
    	self.myConn = GameConnection()

    def buildProtocol(self, addr):
    	return self.myConn

if __name__ == '__main__':

	reactor.listenTCP(START_PORT, StartFactory()) #listen on the starting port to wait for player to join

	reactor.run()