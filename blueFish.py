class blueFish(pygame.sprite.Sprite):
    def __init__(self, gs, ycoord, direction):
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.direction = direction
        self.rect.y = ycoord
        if self.direction == "left":
            self.rect.x = 640
        else:
            self.rect.x = 0
    def move(self):
        if(self.direction == "left"):
            self.rect.x -= 1
        else:
            self.rect.x += 1
