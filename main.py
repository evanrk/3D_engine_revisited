import pygame
import sys

from vectors import *
from render_helper import *
from constants import *
from camera import *

pygame.init()

aspect_ratio = WINDOW_WIDTH/WINDOW_HEIGHT


window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("3D Engine Pt 2!!")


# cube vectors

# x vectors for cube
cube_vec3 = Vector3((1, 0, 0), (0, 0, 0), color=(255, 255, 255))
cube_vec4 = Vector3((1, 0, 0), (0, 1, 0), color=(255, 255, 255))
cube_vec2 = Vector3((1, 0, 0), (0, 0, 1), color=(255, 255, 255))
cube_vec1 = Vector3((1, 0, 0), (0, 1, 1), color=(255, 255, 255))

# y vectors for cube
cube_vec5 = Vector3((0, 1, 0), (0, 0, 0), color=(255, 255, 255))
cube_vec6 = Vector3((0, 1, 0), (0, 0, 1), color=(255, 255, 255))
cube_vec8 = Vector3((0, 1, 0), (1, 0, 0), color=(255, 255, 255))
cube_vec7 = Vector3((0, 1, 0), (1, 0, 1), color=(255, 255, 255))

# z vectors for cube
cube_vec9  = Vector3((0, 0, 1), (0, 0, 0), color=(255, 255, 255))
cube_vec10 = Vector3((0, 0, 1), (1, 0, 0), color=(255, 255, 255))
cube_vec12 = Vector3((0, 0, 1), (0, 1, 0), color=(255, 255, 255))
cube_vec11 = Vector3((0, 0, 1), (1, 1, 0), color=(255, 255, 255))

vecs = [
    cube_vec1,
    cube_vec2,
    cube_vec3,
    cube_vec4,
    cube_vec5,
    cube_vec6,
    cube_vec7,
    cube_vec8,
    cube_vec9,
    cube_vec10,
    cube_vec11,
    cube_vec12,
]

# creates 3 axis
x_vec = Vector3((1, 0, 0), (0, 0, 1), color=(255, 0, 0))
y_vec = Vector3((0, 1, 0), (0, 0, 1), color=(0, 255, 0))
z_vec = Vector3((0, 0, 1), (0, 0, 1), color=(0, 0, 255))

vecs = [
    x_vec,
    y_vec,
    z_vec,
]

# normal vec of camera


camera_normal = Vector3((0, 0, 1))
camera_perpendicular_x = Vector3((1, 0, 0))
camera_pos = (0, 0, -1)

camera = Camera(camera_normal, camera_perpendicular_x, camera_pos)

# camera_normal, camera_perpendicular_x = rotate_camera(camera_normal, camera_perpendicular_x, theta_z=45, theta_y=45)

run = True
while run:
    run = is_on()

    # handle key presses
    # keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_UP] or keys[pygame.K_w]:
    #     camera_normal = translate_vector(camera_normal, camera_normal/60)
    # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    #     camera_normal = translate_vector(camera_normal, camera_normal/-60)
    # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #     camera_normal = translate_vector(camera_normal, camera_perpendicular_x/-60)
    # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    #     camera_normal = translate_vector(camera_normal, camera_perpendicular_x/60)
    # if keys[pygame.K_q] or keys[pygame.K_d]:
    #     camera_normal = translate_vector(camera_normal, camera_normal.cross(camera_perpendicular_x)/60)
    # if keys[pygame.K_e] or keys[pygame.K_d]:
    #     camera_normal = translate_vector(camera_normal, camera_normal.cross(camera_perpendicular_x)/-60)
    

    # color background black
    window.fill((0, 0, 0))

    # draw_line_2d(window, Vector2((500, 0), (-250, 0), color=(255, 0, 255)))

    # draw a cube
    # camera.one_point_perspective(window, cube_vec10)
    # camera.one_point_perspective(window, cube_vec1)
    # camera.one_point_perspective(window, cube_vec2)
    # camera.one_point_perspective(window, cube_vec3)
    # camera.one_point_perspective(window, cube_vec4)
    # camera.one_point_perspective(window, cube_vec5)
    # camera.one_point_perspective(window, cube_vec6)
    # camera.one_point_perspective(window, cube_vec7)
    # camera.one_point_perspective(window, cube_vec8)
    # camera.one_point_perspective(window, cube_vec9)
    # camera.one_point_perspective(window, cube_vec11)
    # camera.one_point_perspective(window, cube_vec12)

    camera.draw_vecs_3d(window, vecs)
    vecs = rotate_vecs(vecs, theta_y=1, theta_z=1, in_position=False)
    
    # camera.one_point_perspective(window, (0, 0, 255), z_vec)
    # camera.one_point_perspective(window, (255, 0, 0), x_vec)
    # camera.one_point_perspective(window, (0, 255, 0), y_vec)

    # rotates the camera by 1 degree around the y axis
    # camera.rotate(camera_normal, camera_perpendicular_x, theta_y=1)


    # update display
    pygame.display.flip()

    # cap framerate
    pygame.time.Clock().tick(60)

# # cleanup
pygame.quit()
sys.exit()