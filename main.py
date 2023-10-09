import pygame
import sys

from vectors import *
from pygame_helper import *
from constants import *

pygame.init()

aspect_ratio = WINDOW_WIDTH/WINDOW_HEIGHT


window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("3D Engine Pt 2!!")

# test_vec1 = Vector3((1, 0, 0), start_pos=(0, 0, 0)) * 50

cube_vec1 = Vector3((1, 0, 0), (0, 50, 50)) * 50
cube_vec2 = Vector3((1, 0, 0), (0, 0, 50)) * 50
cube_vec3 = Vector3((1, 0, 0), (0, 0, 0)) * 50
cube_vec4 = Vector3((1, 0, 0), (0, 50, 0)) * 50

cube_vec5 = Vector3((0, 1, 0), (0, 0, 0)) * 50
cube_vec6 = Vector3((0, 1, 0), (0, 0, 50)) * 50
cube_vec7 = Vector3((0, 1, 0), (50, 0, 50)) * 50
cube_vec8 = Vector3((0, 1, 0), (50, 0, 0)) * 50

cube_vec9 = Vector3((0, 0, 1), (0, 0, 0)) * 50
cube_vec10 = Vector3((0, 0, 1), (50, 0, 0)) * 50
cube_vec11 = Vector3((0, 0, 1), (50, 50, 0)) * 50
cube_vec12 = Vector3((0, 0, 1), (0, 50, 0)) * 50

camera_normal = Vector3((1, 0, 0))

run = True
while run:
    run = is_on()

    # color background black
    window.fill((0, 0, 0))

    draw_line_3d(window, (255, 255, 255), cube_vec1, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec2, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec3, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec4, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec5, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec6, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec7, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec8, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec9, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec10, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec11, camera_normal)
    draw_line_3d(window, (255, 255, 255), cube_vec12, camera_normal)
    
    camera_normal = rotate_vector(camera_normal, theta_z=1/6)

    # update display
    pygame.display.flip()

    # cap framerate
    pygame.time.Clock().tick(60)


# cleanup
pygame.quit()
sys.exit()