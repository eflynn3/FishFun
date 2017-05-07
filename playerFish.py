import pygame

class playerFish(pygame.sprite.Sprite):
    def __init__(self, gs, sz):
        self.image = pygame.image.load("playerSmall.png")
        #self.image = pygame.transform.scale(self.image, (40, 20))
        self.size = sz
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.points = 0

    def move(self, xc, yc):
        self.rect.x += xc
        self.rect.y += yc

    def add_points(self, points):
        self.points += points
    
    def change_size(self):
        self.size += 5
        #self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.image.load("playerMedium.png")
        
    def tick(self):
        pass
    
