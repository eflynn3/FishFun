import sys
import pygame
import math

class GameSpace:
    def main(self):
        pygame.init()

        oceanImage = pygame.image.load("oceanBackground.png")
        self.size = self.width, self.height = 800,600
        self.black = 0,0,0
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(oceanImage, [0,0])
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
            pygame.display.flip()
        pygame.display.set_caption("Fish Fun")
        self.screen.fill(self.black)

        #instantiate objects

        #self.clock = pygame.tick.Clock()
        #pygame.key.set_repeat(1, 10)
        #while(1):
        #    self.clock.tick(60)
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            sys.exit()

        #    self.screen.fill(self.black)
            #blit
        #    pygame.display.flip()
        #pygame.blit(oceanImage, (0,0))
if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
