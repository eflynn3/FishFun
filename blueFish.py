import pygame

class blueFish(pygame.sprite.Sprite):
    def __init__(self, gs, ycoord, direction):
        self.image = pygame.image.load("blueFish.png")
        self.image = pygame.transform.scale(self.image, (60, 60)) 
        self.rect = self.image.get_rect(center = (50, 50))

        self.direction = direction
        self.rect.y = ycoord
        if self.direction == "left":
            self.rect.x = 640
        else:
            self.rect.x = 0
    
    def tick(self):
        if(self.direction == "left"):
            self.rect.x -= 1
        else:
            self.rect.x += 1  

        