import sys
import pygame
import math
from blueFish import blueFish

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
        self.blueFish = blueFish(self, 50, "left")

        done = False
        pygame.key.set_repeat(1, 10)
        while not done:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

            self.blueFish.tick()
            #self.screen.fill(oceanImage)
            self.screen.blit(oceanImage, (0,0))
            self.screen.blit(self.blueFish.image, self.blueFish.rect)
            pygame.display.flip()

        #game.display.set_caption("Fish Fun")
        #self.screen.fill(self.black)

        #    self.screen.fill(self.black)
        #    pygame.display.flip()
        #pygame.blit(oceanImage, (0,0))

if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
