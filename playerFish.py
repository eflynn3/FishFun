#Programming paradigms
#Playerfish.py where data is stored to be sent for each player gamespace 
#Erin Flynn and Erin Turley

import pygame
class playerFish(pygame.sprite.Sprite):
    def __init__(self, gs, player):
        self.player = player
        self.image = pygame.image.load("playerOriginal.png") #load first image player 1
        self.image2 = pygame.image.load("secondPlayerOriginal.png") #load first image player 2
        self.rect = self.image.get_rect() #create rect for player 1
        self.rect.x = 50
        self.rect.y = 50

        self.rect2 = self.image2.get_rect() #create rect for player 2
        self.rect2.x = 500
        self.rect2.y = 50

        self.points = 0 # set points for player 1
        self.points2 = 0 #set points for player 2
        self.end = 0 #set boolean for game over 
        self.gs = gs #gamespace 
        self.size_score = 0 #set score for fish to change sizes 

    #move each player fished based on the player number passed in 
    def move(self, xc, yc, player):
        if player == "1":
            self.rect.x += xc
            self.rect.y += yc

        elif player == "2":
            self.rect2.x += xc
            self.rect2.y += yc
    
    #change the size of each player fish depending on the fish collision
    def change_size(self, eat_score, f, player):
        if player == "1":
            if self.size_score >= eat_score: 
                if eat_score == 0:  #red fish 
                    if eat_score + 1 == self.size_score:
                        self.image = pygame.image.load("playerSmall.png") #update image
                        self.gs.image = "playerSmall.png" #update image in gs for passing data
                    self.points += (eat_score + 2) #update points 
                    self.gs.points += (eat_score + 2) #update points in gs for passing data
                    pygame.sprite.Sprite.kill(f) #remove sprite collided with

                elif eat_score  == 2: #green fish 
                    if eat_score + 1 == self.size_score: 
                        self.image = pygame.image.load("playerMedium.png") #update image
                        self.gs.image = "playerMedium.png" #update image for passing data

                    self.points += (eat_score + 2) #update score 
                    self.gs.points += (eat_score + 2) #update score for passing data
                    pygame.sprite.Sprite.kill(f) #remove sprite collided with 

                elif eat_score == 4: #blue fish 
                    if eat_score == self.size_score:
                        self.image = pygame.image.load("playerLarge.png") #update image
                        self.gs.image = "playerLarge.png" #update image for passing data
                    
                    self.points += (eat_score + 2) #update score 
                    self.gs.points += (eat_score + 2) #update score for passing data
                    pygame.sprite.Sprite.kill(f) #remove sprite collided with 

                elif eat_score == 6: #gold fish 
                    if eat_score == self.size_score:
                        self.image = pygame.image.load("playerBiggest.png") #update image
                        self.gs.image = "playerBiggest.png" #update image for passing data
                
                    self.points += (eat_score + 2) #update score
                    self.gs.points += (eat_score + 2) #update score for passing data
                    pygame.sprite.Sprite.kill(f) #remove sprite collided with 
                elif eat_score == 8: #shark
                    self.end = 1 #set in for second scree
                    self.gs.end_game() #game is over
            
            else:
                self.end = 1 #set for second screen
                self.gs.end_game() #game is over
            
            self.size_score += 1 #increment the size score of the fish 
 
        elif player == "2":
            if self.size_score >= eat_score:
                if eat_score == 0:  #red fish 
                    if eat_score + 1 == self.size_score:
                        self.image2 = pygame.image.load("secondPlayerSmall.png") #update image
                        self.gs.image2 = "secondPlayerSmall.png" #update image for passing data
                    
                    self.points2 += (eat_score + 2) #update score
                    self.gs.points2 += (eat_score + 2) #update score for passing data
                    pygame.sprite.Sprite.kill(f) #remove sprite collided with

                elif eat_score == 2: #green fish 
                    if eat_score + 1 == self.size_score:
                        self.image2 = pygame.image.load("secondPlayerMedium.png")#update image
                        self.gs.image2 = "secondPlayerMedium.png"  #update image for passing data

                    self.points2 += (eat_score + 2) #update score
                    self.gs.points2 += (eat_score + 2) #update score for passing data

                    pygame.sprite.Sprite.kill(f) #remove sprite collided with

                elif eat_score == 4: #blue fish 
                    if eat_score == self.size_score:
                        self.image2 = pygame.image.load("secondPlayerLarge.png") #update image
                        self.gs.image2 = "secondPlayerLarge.png" #update image for passing data
                
                    self.points2 += (eat_score + 2) #update score
                    self.gs.points2 += (eat_score + 2) #update score for passing data

                    pygame.sprite.Sprite.kill(f) #remove sprite collided with

                elif eat_score == 6: #gold fish 
                    if eat_score == self.size_score:
                        self.image2 = pygame.image.load("secondPlayerBiggest.png") #update image
                        self.gs.image2 = "secondPlayerBiggest.png" #update image for passing data
          
                    self.points2 += (eat_score + 2) #update score
                    self.gs.points2 += (eat_score + 2) #update score for passing data

                    pygame.sprite.Sprite.kill(f) #remove sprite collided with
                elif eat_score == 8: #shark
                    self.end = 1
                    self.gs.end_game() #game over 
            
            else:
                self.end = 1
                self.gs.end_game() # game over
            
            self.size_score += 1 #increment the size score of fish 
    
    #every loop check if the player has collided with an enemy fish
    def tick(self, player, connection):
        if player == "1":
            for f in self.gs.fishes:
                if self.rect.colliderect(f.rect):
                    self.gs.remove_sprite = f.sprite_id #update data for passing 
                    self.change_size(f.eat_score, f, player) #update fish 
        if player == "2":
            for f in self.gs.fishes:
                if self.rect2.colliderect(f.rect):
                    self.gs.remove_sprite = f.sprite_id #update data for passing 
                    self.change_size(f.eat_score, f, player)  #update fish          
    
