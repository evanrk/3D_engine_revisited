import math

import pygame
import numpy as np

from vectors import *
from constants import *

def is_on():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def rotate_vector(vector:Vector3, theta_x=0, theta_y=0, theta_z=0):
    """angles in degrees"""
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
    
    return Vector3(rotation_x_matrix @ rotation_y_matrix @ rotation_z_matrix @ vector.values)


def draw_line_2d(surface, color, vector:Vector2):
    translated_start = (vector.start_pos[0] + WINDOW_WIDTH/2, vector.start_pos[1] + WINDOW_HEIGHT/2)
    translated_end = (vector.end_pos[0] + WINDOW_WIDTH/2, vector.end_pos[1] + WINDOW_HEIGHT/2)

    pygame.draw.line(surface, color, translated_start, translated_end)


def draw_line_3d(surface, color, vector:Vector3, camera_normal:Vector3):
    # projection = vector - camera_normal.proj(vector)
    # x = projection.x
    # y = projection.y

    # print(projection)

    # position_projection = Vector3(vector.start_pos) - camera_normal.proj(Vector3(vector.start_pos))
    # pos_start_x = position_projection.x
    # pos_start_y = position_projection.y

    # draw_line_2d(surface, color, Vector2((x, y), (pos_start_x, pos_start_y)))


    rotate_x_angle = math.degrees(math.atan(camera_normal.y/math.sqrt(camera_normal.z**2 + camera_normal.x**2))) if camera_normal.z + camera_normal.x != 0 else 90
    rotate_y_angle = math.degrees(math.atan(camera_normal.x/math.sqrt(camera_normal.z**2 + camera_normal.y**2))) if camera_normal.z + camera_normal.y != 0 else 90

    rotated_vec = rotate_vector(vector, theta_x=rotate_x_angle, theta_y=rotate_y_angle)
    x = rotated_vec.x
    y = rotated_vec.y

    # TODO: change
    start_pos_x = 0
    start_pos_y = 0

    draw_line_2d(surface, color, Vector2((x, y), (start_pos_x, start_pos_y)))