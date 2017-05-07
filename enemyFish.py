import pygame

class enemyFish(pygame.sprite.Sprite):
    def __init__(self, gs, yc, direction, filename, sz):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (sz, sz)) #30 
        self.rect = self.image.get_rect(center = (50, 50))
        self.size = sz

        self.direction = direction
        self.rect.y = yc
        if self.direction == "left":
            self.rect.x = 640
        else:
            self.rect.x = 0
    
    def update(self):
        if(self.direction == "left"):
            self.rect.x -= 2
        else:
            self.rect.x += 2
        if self.rect.colliderect(self.gs.playerFish.rect):
            if self.gs.playerFish.size >= self.size:
                self.gs.playerFish.change_size()
#                pygame.sprite.Sprite.kill(self)#not working
            else:
                self.gs.end_game()
