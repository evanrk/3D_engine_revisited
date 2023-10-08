import pygame
import sys

from vectors import *
from pygame_helper import *

pygame.init()

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500
window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("3D Engine Pt 2!!")

run = True
while run:
    run = is_on()

    # color background black
    window.fill((0, 0, 0))
    
    # update display
    pygame.display.flip()

    # cap framerate
    pygame.time.Clock().tick(60)


# cleanup
pygame.quit()
sys.exit()