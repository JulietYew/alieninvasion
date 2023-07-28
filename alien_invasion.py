#a ship that fires bullet
#a 2D game
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet_allien import Bullet
from alien import Alien
class AlienInvasion:
#overall class to manage game assets and behaviour.

    def __init__(self):
#initialize the game and get game resources
        pygame.init()

        self.settings = Settings()
#here we imported a class called Settings and then we create a new instance and assign it to the class Settings

        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
#here we called the instance of the Settings class with the attributes that were defined
        self.background = pygame.transform.smoothscale(self.settings.background, (1200, 720))

#setting the game to a full screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height= self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion ")
#setting the color of the game as RGB colors
        #self.bg_color = (230, 230,230)

        self.ship = Ship(self)
#here we are calling the class Ship into the class AlienInvasion(it has already been stated on how to do that
    #but it requires one argument self which refers to the current instance of the class AlienInvasion

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    #we use the pygame.sprite.Group() that automatically draws the image to the screen
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            # deleting old bullets to reduce space
    def _update_bullets(self):
        """ we created a new method to make the code neat and update the bullets in groups of three when fired"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))




    def _check_events(self):

         # checking for events. PS: the for loop is an event loop
        for event in pygame.event.get():
            # to access the events that the pygame detects, we use the pygame.event.get() function

            if event.type == pygame.QUIT:
                sys.exit()
#we created two helper methods from the method run_game(_check_events and _update_screen).
            elif event.type == pygame.KEYDOWN:
# a pygame keydown event is a key that has been pressed or activated
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                # we added a new elif for when a user presses the space tab to fire bullets
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
    #a pygame keyup event is a key detected by pygame when an arrow key has been released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_q:
                    sys.exit()
                    #move the ship to the right
                    #self.ship.rect.x +=1


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
         self.screen.blit(self.background, (0, 0))
         self.ship.blitme()
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.aliens.draw(self.screen)
         pygame.display.flip()

         # to make the aliens appear we call the draw() function

# we will now refactor the def_create_fleet function
    def _create_fleet(self):
        """ create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # we want to get the width of the alien and the number of aliens that can fit in a row
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // 2 * alien_width

        # to determine the number of aliens that can fit in a screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height- (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

       # to create multiple rows of aliens , we use a nested for loop
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        # create the first row of aliens
    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien_width = alien.rect.width
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)



        #updates the screen of the game with respect to the positions


if __name__ == '__main__':
    #creating an instance of the class AlienInvasion
    ai = AlienInvasion()
    ai.run_game()