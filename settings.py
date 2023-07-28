import pygame


class Settings:
    #a class to store all settings of the class AlienInvasion
    def __init__(self):
    #initialize the game settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (0,0,0)
        self.background = pygame.image.load('images/unsplash.jpg')
        self.default_image_screen = (1200, 720)
    #adjusting the ship's speed by adding an attribute
        self.ship_speed = 1.5

        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3