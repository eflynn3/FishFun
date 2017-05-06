import pygame

class playerFish(pygame.sprite.Sprite):
    def __init__(self, gs, sz):
        self.image = pygame.image.load("playerFish.png")
        self.image = pygame.transform.scale(self.image, (sz, sz))
        self.size = sz
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
    def move(self, xc, yc):
        self.rect.x += xc
        self.rect.y += yc
    def change_size(self):
        self.size += 5
        self.image = pygame.transform.scale(self.image, (size, size))
        
    def tick(self):
        pass
    
