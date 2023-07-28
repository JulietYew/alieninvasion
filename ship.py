import pygame
class Ship:
    def __init__(self, ai_game):
#this method will take another parameter which is the instance of the class AlienInvasion to get access
#to the game resoruces"""

#to display the ship image on the screen and call the get_rect() function to put the ship in the correct position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #to load the image and give it the location of our ship image
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
#starting each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

#storing a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

#movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        #update the ship's position based on the movement flag
        #update the ship's x value not the rect()
        # to limit the range of the ship so it won't pass the screen edges
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed

            #update rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        #draws the image of the ship to the screen at the current location
        self.screen.blit(self.image, self.rect)


