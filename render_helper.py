import math
import sys

import pygame
import numpy as np

from vectors import *
from constants import *

def is_on():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def translate_vector(vector:Vector3, translate_vector:Vector3):
    return Vector3(vector.values, (vector.start_pos[0] + translate_vector.x, vector.start_pos[1] + translate_vector.y, vector.start_pos[2] + translate_vector.z))


def rotate_vector(vector:Vector3, theta_x=0, theta_y=0, theta_z=0, in_position=False):
    """Rotates a vector around the x-axis, y-axis, and z-axis. Angles in degrees"""
    # convert to radians
    theta_x = math.radians(theta_x)
    theta_y = math.radians(theta_y)
    theta_z = math.radians(theta_z)


    cos_x = math.cos(theta_x)
    sin_x = math.sin(theta_x)
    rotation_x_matrix = np.array([
        [1, 0, 0],
        [0, cos_x, -sin_x],
        [0, sin_x, cos_x]
        ])
    
    cos_y = math.cos(theta_y)
    sin_y = math.sin(theta_y)
    rotation_y_matrix = np.array([
        [cos_y, 0, sin_y],
        [0, 1, 0],
        [-sin_y, 0, cos_y]
    ])
    
    cos_z = math.cos(theta_z)
    sin_z = math.sin(theta_z)
    rotation_z_matrix = np.array([
        [cos_z, -sin_z, 0],
        [sin_z, cos_z, 0],
        [0, 0, 1],
    ])
    
    return Vector3(rotation_z_matrix @ rotation_y_matrix @ rotation_x_matrix @ vector.values, vector.start_pos) \
        if not in_position \
        else Vector3(rotation_z_matrix @ rotation_y_matrix @ rotation_x_matrix @ vector.values, 
                         rotation_z_matrix @ rotation_y_matrix @ rotation_x_matrix @ vector.start_pos)


def draw_line_2d(surface, color, vector:Vector2):
    """Draw 2d vector with coordinates at center"""
    translated_start = (vector.start_pos[0]*50 + WINDOW_WIDTH/2, -vector.start_pos[1]*50 + WINDOW_HEIGHT/2)
    translated_end = (vector.end_pos[0]*50 + WINDOW_WIDTH/2, -vector.end_pos[1]*50 + WINDOW_HEIGHT/2)

    pygame.draw.line(surface, color, translated_start, translated_end)


#TODO: FINISH OFF SCREEN CHECK
# def off_screen_check(surface, color, vector:Vector3, camera_normal:Vector3):
#     if camera_normal.x > 0:
        
#     if camera_normal.y > 0:
    
#     if camera_normal.z > 0:
    
    # one_point_perspective(surface, color, rotated_vec, rotated_start_pos.values, camera_normal)


# def one_point_perspective(surface, color, vector:Vector3):
#     """Project onto a one point perspective. Condenses points based on z value"""
#     # z axis is out/in the screen
    
#     start_pos_x = vector.start_pos[0]
#     start_pos_y = vector.start_pos[1]
#     start_pos_z = vector.start_pos[2]
#     # start_pos_z = vector.start_pos[2]/10

#     end_pos_x = vector.end_pos[0]
#     end_pos_y = vector.end_pos[1]
#     end_pos_z = vector.end_pos[2] / vector.magnitude
#     # end_pos_z = vector.end_pos[2]/10

#     # tan gives the ratio for distance to x size <--- IMPORTANT
#     proj_start_pos_x = start_pos_x / (math.tan(FOV/2) * start_pos_z)
#     proj_start_pos_y = start_pos_y / (math.tan(FOV/2) * start_pos_z)
    
#     proj_end_pos_x = end_pos_x / (math.tan(FOV/2) * end_pos_z)
#     proj_end_pos_y = end_pos_y / (math.tan(FOV/2) * end_pos_z)

#     # create new vector2d
#     vector_length_values = (proj_end_pos_x - proj_start_pos_x, proj_end_pos_y - proj_start_pos_y)
#     start_values = (proj_start_pos_x, proj_start_pos_y)
    
#     perspective_vector = Vector2(vector_length_values, start_pos=start_values)
    
#     # draw new 2d vector
#     draw_line_2d(surface, color, perspective_vector)