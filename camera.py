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
    

    def translate(self, x, y, z):
        self.camera_normal = translate_vector(self.camera_normal, Vector3((x, y, z))/60)
        self.camera_x = translate_vector(self.camera_x, Vector3((x, y, z))/60)


    def rotate(self, theta_x=0, theta_y=0, theta_z=0):
        """rotates the camera on all 3 axis"""
        self.camera_normal = rotate_vector(self.camera_normal, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z)
        self.camera_x = rotate_vector(self.camera_x, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z)
    
    
    
    def draw_line_3d(self, surface, vector:Vector3):
        # the magnitude in the direction of the camera perp vector should be the distance of that vector in the projected x direction
        projection_x = self.camera_x.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        # same for this one but in the y direction
        projection_y = self.camera_y.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        
        projection_z = self.camera_normal.proj_scalar(vector - Vector3(self.camera_normal.start_pos))

        edge_x = max(math.tan(FOV/2) * projection_z, 0)
        edge_y = max(math.tan(FOV/2) * projection_z * WINDOW_WIDTH/WINDOW_HEIGHT, 0) # scaled bc height is smaller


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
        

        # the distance to the start of the vector
        distance_to_start = (vector_start - Vector3(self.camera_normal.start_pos)).magnitude
        # the distance to the end of the vector
        distance_to_end = (vector_end - Vector3(self.camera_normal.start_pos)).magnitude

        print(f"{distance_to_start=}\n{distance_to_end=}")

        # scaled start and end from the fov
        scaler_start = (math.tan(FOV/2) * distance_to_start)
        scaler_end = (math.tan(FOV/2) * distance_to_end)

        # scaled to perspective
        perspective_start = vector_start / scaler_start
        perspective_end = vector_end / scaler_end

        # create perspective vector from the new start and end values
        perspective_vector = Vector3((perspective_end-perspective_start).values, perspective_start.values, color=vector.color)


        self.draw_line_3d(surface, perspective_vector)


    def draw_vecs_3d(self, surface, vecs):
        for vec in vecs:
            self.draw_line_3d(surface, vec)


    def draw_vecs_1p(self, surface, vecs):
        for vec in vecs:
            self.one_point_perspective(surface, vec)



# legacy one point perspective (scales very weirdly and i can figure it out haha)
 # def one_point_perspective(self, surface, vector:Vector3):
    #     """Project onto a one point perspective. Condenses points based on z value"""
    #     # z axis is out/in the screen
        
    #     start_pos_x = vector.start_pos[0] - self.camera_normal.start_pos[0]
    #     start_pos_y = vector.start_pos[1] - self.camera_normal.start_pos[1]
    #     start_pos_z = (vector.start_pos[2] - self.camera_normal.start_pos[2])
    #     # start_pos_z = vector.start_pos[2]/10

    #     end_pos_x = vector.end_pos[0] - self.camera_normal.start_pos[0]
    #     end_pos_y = vector.end_pos[1] - self.camera_normal.start_pos[1]
    #     end_pos_z = (vector.end_pos[2] - self.camera_normal.start_pos[2])
    #     # end_pos_z = vector.end_pos[2]/10

    #     # tan gives the ratio for distance to x size <--- IMPORTANT
    #     proj_start_pos_x = start_pos_x / (math.tan(FOV/2) * start_pos_z)
    #     proj_start_pos_y = start_pos_y / (math.tan(FOV/2) * start_pos_z)
        
    #     proj_end_pos_x = end_pos_x / (math.tan(FOV/2) * end_pos_z)
    #     proj_end_pos_y = end_pos_y / (math.tan(FOV/2) * end_pos_z)

    #     # create new vector2d
    #     vector_length_values = (proj_end_pos_x - proj_start_pos_x, proj_end_pos_y - proj_start_pos_y)
    #     start_values = (proj_start_pos_x, proj_start_pos_y)
        
    #     perspective_vector = Vector2(vector_length_values, start_pos=start_values, color=vector.color)
        
    #     # draw new 2d vector
    #     draw_line_2d(surface, perspective_vector)