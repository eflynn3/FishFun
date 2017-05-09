import sys
import pygame
import math
#from enemyFish import blueFish
#from enemyFish import greenFish
from enemyFish import enemyFish
from playerFish import playerFish

class GameSpace:
    def main(self):
        #initialize gamespace
        pygame.init()
        self.clock = pygame.time.Clock()
        self.oceanImage = pygame.image.load("oceanBackground.png")
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.oceanImage, [0,0])

        self.fishes = pygame.sprite.Group()
        # initialize all game objects
        self.playerFish = playerFish(self, 15)      #set size to 15
        
        self.pinkFish = enemyFish(self, 20, "right", "pinkFish.png", 15, 2, 0)
        self.pinkFish2 = enemyFish(self, 200, "left", "pinkFish.png", 15, 1, 0)
        self.pinkFish3 = enemyFish(self, 240, "right", "pinkFish.png", 15, 4, 0)
        self.blueFish = enemyFish(self, 50, "left", "blueFish.png", 60, 1, 4)

        self.blueFish = enemyFish(self, 50, "left", "blueFish.png", 60, 1, 4)
        self.blueFish2 = enemyFish(self, 400, "left", "blueFish.png", 60, 5, 4)
        self.blueFish3 = enemyFish(self, 320, "right", "blueFish.png", 60, 3, 4)

        self.greenFish = enemyFish(self, 150, "right", "greenFish.png", 35, 4, 2)
        self.greenFish2 = enemyFish(self, 260, "left", "greenFish.png", 35, 1, 2)
        self.greenFish3 = enemyFish(self, 500, "right", "greenFish.png", 35, 2, 2)

        self.goldFish = enemyFish(self, 200, "left", "goldFish.png", 120, 3, 6)
        self.goldFish2 = enemyFish(self, 450, "left", "goldFish.png", 120, 5, 6)
        self.goldFish3 = enemyFish(self, 340, "right", "goldFish.png", 120, 2, 6)

        self.shark1 = enemyFish(self, 418, "right", "shark3.png", 150, 3, 8)

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

        
        done = False
        pygame.key.set_repeat(1, 10)
        while not done: #eventually get rid of this
            self.game_loop()
        #game.display.set_caption("Fish Fun")
        #self.screen.fill(self.black)

    def end_game(self):
        self.screen.blit(self.oceanImage, (0,0))
        mytext = pygame.font.SysFont("monospace", 20)
        label = mytext.render("You Lost!", 1, (255, 255, 0))
        self.screen.blit(label, (100, 100))
        pygame.display.flip()
        pygame.time.wait(5000)
        #sys.exit()

    def game_loop(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.playerFish.move(0, 5)
                elif event.key == pygame.K_UP:
                    self.playerFish.move(0, -5)
                elif event.key == pygame.K_RIGHT:
                    self.playerFish.move(5, 0)
                elif event.key == pygame.K_LEFT:
                    self.playerFish.move(-5, 0)
                    
        self.playerFish.tick()
        self.fishes.update()
        #pygame.sprite.spritecollide(self.playerFish, self.fishes, True)

        self.screen.blit(self.oceanImage, (0,0))
        self.fishes.draw(self.screen)
        #points
        mytext = pygame.font.SysFont("monospace", 20)
        score = "Score: " + str(self.playerFish.points)
        label = mytext.render(score, 1, (0, 0, 0))
        self.screen.blit(label, (675, 30))
        self.screen.blit(self.playerFish.image, self.playerFish.rect)
        pygame.display.flip()

        
if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
