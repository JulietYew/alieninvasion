import sys
import pygame
class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("Pygame File")

    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print("A key has been pressed")
            pygame.display.flip()

if __name__ == '__main__':
    py = Screen()
    py.run_screen()

