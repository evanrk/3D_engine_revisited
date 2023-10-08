import pygame

def is_on():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
