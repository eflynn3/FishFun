#Programming Paradigms project
#Gamespace creates screens for the game to be played on 
#Erin Flynn and Erin Turley

import sys
import pygame
import math
from enemyFish import enemyFish
from playerFish import playerFish

class GameSpace:
    def main(self, playerNumber, connection):
        #initialize gamespace
        pygame.init()
        self.playerNumber = playerNumber
        self.oceanImage = pygame.image.load("oceanBackground.png")
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.oceanImage, [0,0])
        self.connection = connection #connection from network
        self.fishes = pygame.sprite.Group() #group of all enemy fish
        self.remove_sprite = 0 #ID for sprite in collision
        self.end = 0 #boolean for if game is over
        self.image2 = "secondPlayerOriginal.png" #starting image player 2
        self.image = "playerOriginal.png" #starting image player 1

        self.points = 0 #player 1 points
        self.points2 = 0 #player 2 points 

        # initialize all game objects
        self.playerFish = playerFish(self, self.playerNumber)      #set size to 15

        # enemy fish input: gamespace, y val, direction, filename, size, speed, eat_score, sprite_id
        self.pinkFish = enemyFish(self, 20, "right", "pinkFish.png", 15, 2, 0, 1)
        self.pinkFish2 = enemyFish(self, 200, "left", "pinkFish.png", 15, 1, 0, 2)
        self.pinkFish3 = enemyFish(self, 240, "right", "pinkFish.png", 15, 4, 0, 3)
        self.blueFish = enemyFish(self, 50, "left", "blueFish.png", 60, 1, 4, 4)

        self.blueFish = enemyFish(self, 50, "left", "blueFish.png", 60, 1, 4, 5)
        self.blueFish2 = enemyFish(self, 400, "left", "blueFish.png", 60, 5, 4, 6)
        self.blueFish3 = enemyFish(self, 320, "right", "blueFish.png", 60, 3, 4, 7)

        self.greenFish = enemyFish(self, 150, "right", "greenFish.png", 35, 4, 2, 8)
        self.greenFish2 = enemyFish(self, 260, "left", "greenFish.png", 35, 1, 2, 9)
        self.greenFish3 = enemyFish(self, 500, "right", "greenFish.png", 35, 2, 2, 10)

        self.goldFish = enemyFish(self, 200, "left", "goldFishFinal.png", 70, 3, 6, 11)
        self.goldFish2 = enemyFish(self, 450, "left", "goldFishFinal.png", 70, 5, 6, 12)
        self.goldFish3 = enemyFish(self, 340, "right", "goldFishFinal.png", 70, 2, 6, 13)

        self.shark1 = enemyFish(self, 418, "right", "shark.png", 100, 3, 8, 14)
        self.shark2 = enemyFish(self, 200, "left", "shark.png", 100, 2, 8, 15)

        #add all enemy fish to group 
        self.fishes.add(self.pinkFish)
        self.fishes.add(self.pinkFish2)
        self.fishes.add(self.pinkFish3)

        self.fishes.add(self.blueFish)
        self.fishes.add(self.blueFish2)
        self.fishes.add(self.blueFish3)

        self.fishes.add(self.greenFish)
        self.fishes.add(self.greenFish2)
        self.fishes.add(self.greenFish3)

        self.fishes.add(self.goldFish)
        self.fishes.add(self.goldFish2)
        self.fishes.add(self.goldFish3)

        self.fishes.add(self.shark1)
        self.fishes.add(self.shark2)

        
        pygame.key.set_repeat(1, 10)

    #function called when game is over 
    def end_game(self):
        self.screen.blit(self.oceanImage, (0,0))
        #display points on the screen 
        mytext = pygame.font.SysFont("monospace", 20)
        score = "Blue: " + str(self.points)
        label = mytext.render(score, 1, (0, 0, 0))
        score2 = "Red: " + str(self.points2)
        label2 = mytext.render(score2, 1, (0, 0, 0))
        self.screen.blit(label, (70, 30))
        self.screen.blit(label2, (600, 30))
        #display game over message 
        mytext = pygame.font.SysFont("monospace", 50)
        label = mytext.render("Game Over!", 1, (255, 255, 0))
        self.screen.blit(label, (250, 200))
        pygame.display.flip()
        sys.exit() #raise exit error to exit program 

    # write data for player 1 to player 2
    def getData(self):
        x = str(self.playerFish.rect.x)
        y = str(self.playerFish.rect.y)
        #create string that will be passed and parsed 
        Str = x + ":" + y + "|" + str(self.remove_sprite) + "#" + self.image + "$" + str(self.points) + "@" + str(self.playerFish.end)
        self.connection.transport.write(Str)
        #reset sprite id to 0 so no value will be removed until set again 
        self.remove_sprite = 0

    # write data for player 2 to player 1
    def getData2(self):
        x = str(self.playerFish.rect2.x)
        y = str(self.playerFish.rect2.y)
        #create string that will be passed and parsed 
        Str = x + ":" + y + "|" + str(self.remove_sprite) + "#" + self.image2 + "$" + str(self.points2) + "@" + str(self.playerFish.end)
        self.connection.transport.write(Str)
        #reset sprite id to 0 so no value will be removed until set again 
        self.remove_sprite = 0

    #set values from the data received in player 2 
    def updateFish(self, data):
        #parse the string for data
        end = data.split("@")[1]
        dat = data.split("@")[0]
        s = dat.split("$")[0]
        score = dat.split("$")[1]
        d = s.split("#")[0]
        img = s.split("#")[1]
        i = d.split("|")[0]
        ID = int(d.split("|")[1])
        x = i.split(":")[0]
        y = i.split(":")[1]

        #set values in the class to update screen to match 
        self.playerFish.rect.x = int(x)
        self.playerFish.rect.y = int(y)
        self.playerFish.image = pygame.image.load(img)
        self.points = int(score)
        self.end = end

        #loop through group to remove sprite if collision occured
        for f in self.fishes:
            if f.sprite_id == ID:
                pygame.sprite.Sprite.kill(f)
    
    #set values from the data received in player 1
    def updateFish2(self, data):
        #parse the string for data        
        end = data.split("@")[1]
        dat = data.split("@")[0]
        s = dat.split("$")[0]
        score = dat.split("$")[1]
        d = s.split("#")[0]
        img = s.split("#")[1]
        i = d.split("|")[0]
        ID = int(d.split("|")[1])
        x = i.split(":")[0]
        y = i.split(":")[1]

        #set values in the class to update screen to match 
        self.playerFish.rect2.x = int(x)
        self.playerFish.rect2.y = int(y)
        self.playerFish.image2 = pygame.image.load(img)
        self.points2 = int(score)
        self.end = end
       
        #loop through group to remove sprite if collision occured
        for f in self.fishes:
            if f.sprite_id == ID:
                pygame.sprite.Sprite.kill(f)

    #loop iterated through like tick in network connection 
    def gameLoop(self):
        #check for kep presses 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.playerFish.move(0, 5,  self.playerNumber)
                elif event.key == pygame.K_UP:
                    self.playerFish.move(0, -5, self.playerNumber)
                elif event.key == pygame.K_RIGHT:
                    self.playerFish.move(5, 0, self.playerNumber)
                elif event.key == pygame.K_LEFT:
                    self.playerFish.move(-5, 0, self.playerNumber)
        #tick on objects    
        self.playerFish.tick(self.playerNumber, self.connection)
        self.fishes.update() #update the enemy fish in the group

        #output to screen 
        self.screen.blit(self.oceanImage, (0,0))
        self.fishes.draw(self.screen)

        #display the points
        mytext = pygame.font.SysFont("monospace", 20)
        score = "Blue: " + str(self.points)
        label = mytext.render(score, 1, (0, 0, 0))
        score2 = "Red: " + str(self.points2)
        label2 = mytext.render(score2, 1, (0, 0, 0))
        self.screen.blit(label, (70, 30))
        self.screen.blit(label2, (600, 30))

        #display the player fish 
        self.screen.blit(self.playerFish.image, self.playerFish.rect)
        self.screen.blit(self.playerFish.image2, self.playerFish.rect2)
        #check if game is over 
        if self.end == "1":
            #output points 
            self.screen.blit(self.oceanImage, (0,0))
            score = "Blue: " + str(self.points)
            label = mytext.render(score, 1, (0, 0, 0))
            score2 = "Red: " + str(self.points2)
            label2 = mytext.render(score2, 1, (0, 0, 0))
            self.screen.blit(label, (70, 30))
            self.screen.blit(label2, (600, 30))
            #ouput game over message
            mytext = pygame.font.SysFont("monospace", 50)
            label = mytext.render("Game Over!", 1, (255, 255, 0))
            self.screen.blit(label, (250, 200))
            pygame.display.flip()
            sys.exit() #raise exit code to end game
        pygame.display.flip()
