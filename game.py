import sys
import pygame
import math
from blueFish import blueFish
from playerFish import playerFish

class GameSpace:
    def main(self):
        #initialize gamespace
        pygame.init()
        self.clock = pygame.time.Clock()
        oceanImage = pygame.image.load("oceanBackground.png")
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(oceanImage, [0,0])

        # initialize all game objects
        self.playerFish = playerFish(self, 15)
        self.blueFish = blueFish(self, 50, "left")

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

            self.blueFish.tick()
            self.screen.blit(oceanImage, (0,0))
            self.screen.blit(self.playerFish.image, self.playerFish.rect)
            self.screen.blit(self.blueFish.image, self.blueFish.rect)
            pygame.display.flip()

        #game.display.set_caption("Fish Fun")
        #self.screen.fill(self.black)

if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
