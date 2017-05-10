import sys
import pygame
import math
#from enemyFish import blueFish
#from enemyFish import greenFish
from enemyFish import enemyFish
from playerFish import playerFish
import cPickle as pickle
import time
class GameSpace:
    def main(self, playerNumber, connection):
        #initialize gamespace
        pygame.init()
        self.playerNumber = playerNumber
        #self.clock = pygame.time.Clock()
        self.oceanImage = pygame.image.load("oceanBackground.png")
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.oceanImage, [0,0])
        self.connection = connection
        self.fishes = pygame.sprite.Group()
        self.remove_sprite = 0
        self.end = 0
        self.image2 = "secondPlayerOriginal.png"
        self.image = "playerOriginal.png"

        self.points = 0
        self.points2 = 0
        # initialize all game objects
        self.playerFish = playerFish(self, self.playerNumber)      #set size to 15

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

        self.shark1 = enemyFish(self, 418, "right", "shark3.png", 90, 3, 8, 14)

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
        
        pygame.key.set_repeat(1, 10)

        #pygame.key.set_repeat(1, 10)
        #while not done: #eventually get rid of this
         #   self.game_loop()
        #game.display.set_caption("Fish Fun")
        #self.screen.fill(self.black)

    def end_game(self):
        self.screen.blit(self.oceanImage, (0,0))
        if self.playerFish.points > self.playerFish.points2:
            text = "Player 1 is the Winner!"
        else:
            text = "Player 2 is the Winner!"

        mytext = pygame.font.SysFont("monospace", 20)
        label = mytext.render(text, 1, (255, 255, 0))
        self.screen.blit(label, (100, 100))
        time.sleep(10)
        pygame.display.flip()
        sys.exit()

    def getData(self):
        x = str(self.playerFish.rect.x)
        y = str(self.playerFish.rect.y)
        Str = x + ":" + y + ":" + str(self.remove_sprite) + ":" + self.image + ":" + str(self.points) + ":" + str(self.playerFish.end)
        self.connection.transport.write(Str)
        self.remove_sprite = 0

    def getData2(self):
        x = str(self.playerFish.rect2.x)
        y = str(self.playerFish.rect2.y)

        Str = x + ":" + y + ":" + str(self.remove_sprite) + ":" + self.image2 + ":" + str(self.points2) + ":" + str(self.playerFish.end)
        self.connection.transport.write(Str)
        self.remove_sprite = 0

    def updateFish(self, data):

        d = data.split(":")
        x = d[0]
        y = d[1]
        ID = d[2]
        img = d[3]
        score = d[4]
        end = d[5]

        self.playerFish.rect.x = int(x)
        self.playerFish.rect.y = int(y)
        self.playerFish.image = pygame.image.load(img)
        self.points = int(score)
        self.end = end

        for f in self.fishes:
            if f.sprite_id == ID:
                pygame.sprite.Sprite.kill(f)

    def updateFish2(self, data):
        d = data.split(":")
        x = d[0]
        y = d[1]
        ID = d[2]
        img = d[3]
        score = d[4]
        end = d[5]

        self.playerFish.rect2.x = int(x)
        self.playerFish.rect2.y = int(y)
        self.playerFish.image2 = pygame.image.load(img)
        self.points2 = int(score)
        self.end = end

        for f in self.fishes:
            if f.sprite_id == ID:
                pygame.sprite.Sprite.kill(f)

    def gameLoop(self):
        #self.clock.tick(60)
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
            
        self.playerFish.tick(self.playerNumber, self.connection)
        
        self.fishes.update()
        if len(self.fishes) == 0:
            self.playerFish.end = 1
        self.screen.blit(self.oceanImage, (0,0))
        self.fishes.draw(self.screen)
        #points
        mytext = pygame.font.SysFont("monospace", 20)
        score = "Blue: " + str(self.points)
        label = mytext.render(score, 1, (0, 0, 0))

        score2 = "Red: " + str(self.points2)
        label2 = mytext.render(score2, 1, (0, 0, 0))
        self.screen.blit(label, (70, 30))
        self.screen.blit(label2, (600, 30))

        self.screen.blit(self.playerFish.image, self.playerFish.rect)
        self.screen.blit(self.playerFish.image2, self.playerFish.rect2)
        pygame.display.flip()

        if self.end == 1:
            print "in"
            self.screen.blit(self.oceanImage, (0,0))
            if self.playerFish.points > self.playerFish.points2:
                text = "Player 1 is the Winner!"
            else:
                text = "Player 2 is the Winner!"

            mytext = pygame.font.SysFont("monospace", 20)
            label = mytext.render(text, 1, (255, 255, 0))
            self.screen.blit(label, (100, 100))
            pygame.display.flip()
            time.sleep(10)
            sys.exit()

