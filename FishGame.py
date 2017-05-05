import pygame, math, time

class GameSpace:
	def main(self):
		#Initialize gamespace
		pygame.init()
		self.size = self.width, self.height = 640, 480
		self.black = 0,0,0
		self.screen = pygame.display.set_mode(self.size)
if __name__ == '__main__':
	gs = GameSpace()
	gs.main()