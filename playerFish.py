import pygame

class playerFish(pygame.sprite.Sprite):
    def __init__(self, gs, player):
        self.player = player
        self.image1 = pygame.image.load("playerOriginal.png")
        #self.image = pygame.transform.scale(self.image, (40, 20))
        self.image2 = pygame.image.load("secondPlayerOriginal.png")
        self.rect = self.image1.get_rect()
        self.rect.x = 50
        self.rect.y = 50

        self.rect2 = self.image2.get_rect()
        self.rect.x = 500
        self.rect.y = 50
        self.points = 0
        self.gs = gs
        self.size_score = 0

    def move(self, xc, yc):
        self.rect.x += xc
        self.rect.y += yc

    def add_points(self, points):
        self.points += points
    
    def change_size(self, eat_score, f):
        print(self.size_score)
        print(eat_score)
        if self.size_score >= eat_score:
            print("in")
            if eat_score == 0:  #red fish 
                if eat_score + 1 == self.size_score:
                    self.image = pygame.image.load("playerSmall.png")
                self.points += (eat_score + 2)
                pygame.sprite.Sprite.kill(f)

            elif eat_score == 2: #green fish 
                if eat_score == self.size_score:
                    self.image = pygame.image.load("playerMedium.png")
                self.points += (eat_score + 2)
                pygame.sprite.Sprite.kill(f)

            elif eat_score == 4: #blue fish 
                if eat_score == self.size_score:
                    self.image = pygame.image.load("playerLarge.png")
                self.points += (eat_score + 2)
                pygame.sprite.Sprite.kill(f)

            elif eat_score == 6: #gold fish 
                if eat_score == self.size_score:
                    self.image = pygame.image.load("playerLarge.png") #need to make another image for this 
                self.points += (eat_score + 2)
                pygame.sprite.Sprite.kill(f)
            elif eat_score == 8: #shark
                self.gs.end_game()
        
        else:
            self.gs.end_game()
        
        self.size_score += 1

    def tick(self):
        for f in self.gs.fishes:
            if self.rect.colliderect(f.rect):
                self.change_size(f.eat_score, f)
    
