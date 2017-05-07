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
        self.pinkFish = enemyFish(self, 20, "right", "pinkFish.png", 15)
        self.blueFish = enemyFish(self, 50, "left", "blueFish.png", 60)
        self.greenFish = enemyFish(self, 150, "right", "greenFish.png", 30)
        self.goldFish = enemyFish(self, 200, "left", "goldFish.png", 120)
        self.fishes.add(self.pinkFish)
        self.fishes.add(self.blueFish)
        self.fishes.add(self.greenFish)
        self.fishes.add(self.goldFish)
        
        done = False
        pygame.key.set_repeat(1, 10)
        while not done:
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

            self.fishes.update()
            pygame.sprite.spritecollide(self.playerFish, self.fishes, True)
#            self.blueFish.tick()
#            self.greenFish.tick()
#            self.pinkFish.tick()
            self.screen.blit(self.oceanImage, (0,0))
            self.fishes.draw(self.screen)
            #points
            text = pygame.font.SysFont("monospace", 20)
            label = text.render(self.playerFish.points, 1, (255, 255, 0))
            self.screen.blit(label, (50, 50))
#            self.screen.blit(self.pinkFish.image, self.pinkFish.rect)
#            self.screen.blit(self.blueFish.image, self.blueFish.rect)
#            self.screen.blit(self.greenFish.image, self.greenFish.rect)
            self.screen.blit(self.playerFish.image, self.playerFish.rect)
            pygame.display.flip()

        #game.display.set_caption("Fish Fun")
        #self.screen.fill(self.black)

    def end_game(self):
        self.screen.blit(self.oceanImage, (0,0))
        mytext = pygame.font.SysFont("monospace", 20)
        label = mytext.render("You Lost!", 1, (255, 255, 0))
        self.screen.blit(label, (100, 100))
        pygame.display.flip()
        pygame.time.wait(5000)
        sys.exit()

if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
