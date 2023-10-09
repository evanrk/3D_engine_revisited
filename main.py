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

# for some reason makes the z axis?????
# test_vec1 = Vector3((1, 1, 1)) * 200
# test_vec2 = Vector3((-1, -1, -1)) * 200

# test_vec3 = Vector3((1, 0, 0)) * 200
# test_vec4 = Vector3((-1, 0, 0)) * 200

# test_vec5 = Vector3((0, 1, 0)) * 200
# test_vec6 = Vector3((0, -1, 0)) * 200

camera_normal = Vector3((1, 0, 0))

run = True
while run:
    run = is_on()

    # color background black
    window.fill((0, 0, 0))

    # draw_line_2d(window, (255, 255, 255), test_vec1)

    draw_line_3d(window, (255, 255, 255), Vector3((0, 0, 1))*50, camera_normal)
    draw_line_3d(window, (255, 255, 255), Vector3((0, 1, 0))*50, camera_normal)
    # camera_normal = camera_normal + Vector3((1, 1, 0)) / 300
    # draw_line_3d(window, (255, 255, 255), test_vec2)
    # draw_line_3d(window, (255, 255, 255), test_vec3)
    # draw_line_3d(window, (255, 255, 255), test_vec4)
    # draw_line_3d(window, (255, 255, 255), test_vec5)
    # draw_line_3d(window, (255, 255, 255), test_vec6)

    camera_normal = rotate_vector(camera_normal, theta_z=1/6)

    # update display
    pygame.display.flip()

    # cap framerate
    pygame.time.Clock().tick(60)

    # #TODO: REMOVE REMOVE REMOVE
    # break


# cleanup
pygame.quit()
sys.exit()