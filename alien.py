import sys

import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()