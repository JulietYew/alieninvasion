import sys
import pygame
from bullet import Set
from rocket import Rocket

class RocketGame:
    def __init__(self):
        pygame.init()
        self.set = Set()
        self.screen = pygame.display.set_mode((self.set.screen_width, self.set.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.rocket = Rocket(self)


    def run_rocket(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.rocket.moving_left = True
                    elif event.key == pygame.K_UP:
                        self .rocket.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.rocket.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.rocket.moving_left = False
                    elif event.key  == pygame.K_UP:
                        self.rocket.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.rocket.moving_down = False
                       # self.rocket.rect.x += 1
                        #mself.rocket.rect.x -= 1



            self.screen.fill(self.set.bg_color)
            self.rocket.blitme()
            pygame.display.flip()

if __name__ == '__main__':
   py = RocketGame()
   py.run_rocket()

