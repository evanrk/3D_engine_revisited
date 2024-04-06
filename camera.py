from vectors import *
from constants import *
from render_helper import *

class Camera:
    def __init__(self, camera_normal:Vector3, camera_x:Vector3, start_pos=(0, 0, 0)):
        self.camera_normal = camera_normal
        self.camera_x = camera_x
        
        self.camera_normal.start_pos = start_pos
        self.camera_x.start_pos = start_pos

    
    @property
    def camera_y(self):
        """property for the camera_y direction (the third camera vector), should save on computing the rotation (double check plz)"""
        camera_y = self.camera_normal.cross(self.camera_x)
        camera_y.start_pos = self.camera_normal.start_pos
        return camera_y
    

    def rotate(camera_normal, camera_x, theta_x=0, theta_y=0, theta_z=0):
        """rotates the camera on all 3 axis"""
        return rotate_vector(camera_normal, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z), \
               rotate_vector(camera_x, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z)
    
    
    
    def draw_line_3d(self, surface, vector:Vector3):
        # the magnitude in the direction of the camera perp vector should be the distance of that vector in the projected x direction
        projection_x = self.camera_x.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        # same for this one but in the y direction
        projection_y = self.camera_y.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        
        projection_z = self.camera_normal.proj_scalar(vector - Vector3(self.camera_normal.start_pos))

        edge_x = max(math.tan(FOV/2) * projection_z, 0)
        edge_y = max(math.tan(FOV/2) * projection_z * WINDOW_WIDTH/WINDOW_HEIGHT, 0) # scaled bc height is smaller

        print(projection_z)

        if abs(projection_x) > abs(edge_x):
            projection_x = math.copysign(edge_x, projection_x)
        
        if abs(projection_y) > abs(edge_y):
            projection_y = math.copysign(edge_x, projection_y)

        # must project the position too
        position_vector = Vector3(vector.start_pos)

        pos_start_x = self.camera_x.proj_scalar(position_vector)
        pos_start_y = self.camera_y.proj_scalar(position_vector)

        draw_line_2d(surface, Vector2((projection_x, projection_y), (pos_start_x, pos_start_y), color=vector.color))


    def one_point_perspective(self, surface, vector:Vector3):
        vector_start = Vector3(vector.start_pos)
        vector_end = (vector + vector_start)
        
        distance_to_start = self.camera_normal.proj_scalar(vector_start)
        distance_to_end = self.camera_normal.proj_scalar(vector_end)

        scaler_start = (math.tan(FOV/2) * distance_to_start)
        scaler_end = (math.tan(FOV/2) * distance_to_end)

        # the magnitude in the direction of the camera perp vector should be the distance of that vector in the projected x direction
        projection_x = self.camera_x.proj_scalar(vector)
        # same for this one but in the y direction
        projection_y = self.camera_y.proj_scalar(vector)


        pos_start_x = self.camera_x.proj_scalar(vector_start)
        pos_start_y = self.camera_y.proj_scalar(vector_start)

        draw_line_2d(surface, Vector2((projection_x, projection_y), (pos_start_x, pos_start_y), color=vector.color))

    
    def draw_vecs_3d(self, surface, vecs):
        for vec in vecs:
            self.draw_line_3d(surface, vec)
