import sys
import pygame
import math

class GameSpace:
    def main(self):
        pygame.init()
        self.size = self.width, self.height = 640,480
        self.black = 0,0,0
        self.screen = pygame.display.set_mode(self.size)
        #instantiate objects

        self.clock = pygame.tick.Clock()
        pygame.key.set_repeat(1, 10)
        while(1):
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.black)
            #blit
            pygame.display.flip()

if __name__ == "__main__":
    gs = GameSpace()
    gs.main()
