#Programming paradigms
#Enemy fish for all fish in game 
#Erin Flynn and Erin Turley

import pygame

class enemyFish(pygame.sprite.Sprite):
    def __init__(self, gs, yc, direction, filename, sz, speed, eat_score, sprite_id):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (sz, sz)) #30 
        self.rect = self.image.get_rect(center = (50, 50))
        self.size = sz #size of fish
        self.yc = yc 
        self.direction = direction
        self.rect.y = yc #starting y coordinate of the fish 
        self.speed = speed  # can specify how fast the fish is moving 
        self.eat_score = eat_score #specifies if it can be eaten or not by player
        self.sprite_id = sprite_id #specifies id so it can be reference for removal
        
        if self.direction == "left":
            self.rect.x = 640 #start sprite on right side of screen
        else:
            self.rect.x = 0
    
    def update(self):
        # move the fish based on inputted speed 
        if(self.direction == "left"):
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        #check if the fish has gone off the screen    
        if self.rect.x < -120 or self.rect.x > 770:
            # if fish is moving left, place on right side 
            if self.direction == "left":
                self.rect.x = 760
            else:
                self.rect.x = -30 #else place on left side 
            self.rect.y = self.yc

            self.gs.fishes.add(self) #add the fish to the group 
