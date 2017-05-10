#Programming paradigms 
#Client.py to create connect to start connection and game connection 
#Erin Flynn and Erin Turley

from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall

from game import GameSpace
import sys

START_PORT = 40111 #port for opening connection
GAME_PORT = 40126 #port for starting connection
HOST = "" #hostname

playGame = GameSpace() #instantiate gamespace 

#connect to the open port in order to join the game 
class StartConnection(Protocol):

    def connectionMade(self):
		print "client connection made"        
    #wait until "start" is recived to then connect to the game port
    def dataReceived(self, data):
        if(data == "start"):
            reactor.connectTCP(HOST, GAME_PORT, GameFactory()) #connect to game port with inputted hostname
        print "client data received"

class StartFactory(ClientFactory):
    def __init__(self):
    	self.myConn = StartConnection()

    def buildProtocol(self, addr):
    	return self.myConn    

    def startedConnecting(self, connector):
        print "Began Initial Connection"

#create connection to game host
class GameConnection(Protocol):
    def connectionMade(self):
        print "connected to game host"
        playGame.main("2", self) #create player 2 gamespace
        gameLoop = LoopingCall(playGame.gameLoop) #loop call for tick
        gameLoop.start(0.0166) #1/60 tick

    #upon receiving data update player 2 scree
    def dataReceived(self, data):
        playGame.updateFish(data) #upon receiving data update player 2 scree
        playGame.getData2() #send data to player one screen 

class GameFactory(ClientFactory):
    def __init__(self):
    	self.myConn = GameConnection()

    def buildProtocol(self, addr):
    	return self.myConn

    def startedConnecting(self, connector):
        print "Began game connection with host"


if __name__ == '__main__':
    HOST = sys.argv[1] #get hostname from input 
    reactor.connectTCP(HOST, START_PORT, StartFactory()) #make connection to the starting port to join the game 

    reactor.run()
