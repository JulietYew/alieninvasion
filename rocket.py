import pygame
class Rocket:
    def __init__(self, rocket_g):
        self.screen = rocket_g.screen
        self.screen_rect = rocket_g.screen.get_rect()
        self.image = pygame.image.load('images\shipe.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        def update(self):
            # update the ship's position based on the movement flag
            # update the ship's x value not the rect()
            # to limit the range of the ship so it won't pass the screen edges
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.x += 1
            if self.moving_left and self.rect.left > 0:
                self.rect.x -= 1

                # update rect object from self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)