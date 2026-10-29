from vectors import *
from constants import *
from render_helper import *

class Camera:
    def __init__(self, camera_normal:Vector3, camera_x:Vector3, start_pos=(0, 0, 0)):
        self.camera_normal = camera_normal
        self.camera_x = camera_x
        
        self.camera_normal.start_pos = start_pos
        self.camera_x.start_pos = start_pos

        self.start_pos = start_pos

    
    @property
    def camera_y(self):
        """property for the camera_y direction (the third camera vector), should save on computing the rotation (double check plz)"""
        camera_y = self.camera_normal.cross(self.camera_x)
        camera_y.start_pos = self.camera_normal.start_pos
        return camera_y
    

    def translate(self, x, y, z):
        """moves the camera in directions with respect to the camera's x, y, z vectors, not the real basis ones"""
        movement_vec = z * self.camera_normal + x * self.camera_x + y * self.camera_y
        self.camera_normal = translate_vector(self.camera_normal, movement_vec / FPS)
        self.camera_x = translate_vector(self.camera_x, movement_vec / FPS)


    def rotate(self, theta_x=0, theta_y=0, theta_z=0):
        """rotates the camera on all 3 axis"""
        self.camera_normal = rotate_vector(self.camera_normal, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z)
        self.camera_x = rotate_vector(self.camera_x, theta_x=theta_x, theta_y=theta_y, theta_z=theta_z)
    
    
    
    def draw_line_3d(self, surface, vector:Vector3):
        # the magnitude in the direction of the camera perp start and end position should be the distance of those vector (points) in the projected x direction
        projection_x_end = self.camera_x.proj_scalar(Vector3(vector.end_pos) - Vector3(self.camera_normal.start_pos))
        projection_x_start = self.camera_x.proj_scalar(Vector3(vector.start_pos) - Vector3(self.camera_normal.start_pos))
        
        # same for this one but in the y direction
        projection_y_end = self.camera_y.proj_scalar(Vector3(vector.end_pos) - Vector3(self.camera_normal.start_pos))
        projection_y_start = self.camera_y.proj_scalar(Vector3(vector.start_pos) - Vector3(self.camera_normal.start_pos))
        
        # projection_z = self.camera_normal.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        # projection_z_start = self.camera_normal.proj_scalar(Vector3(vector.start_pos) - Vector3(self.camera_normal.start_pos))

        # projection_y_start = Vector3(projection_y.start_pos) - Vector3(self.camera_normal.start_pos)
        # projection_z_start = Vector3(projection_z.start_pos) - Vector3(self.camera_normal.start_pos)

        draw_line_2d(surface, Vector2((projection_x_end-projection_x_start, projection_y_end-projection_y_start), (projection_x_start, projection_y_start), color=vector.color))


    # NOTE:
    # 1p_perspective must happen after proj, 3d

    def one_point_perspective(self, surface, vector:Vector3):
        vector_start = Vector3(vector.start_pos)
        vector_end = Vector3(vector.end_pos)
        
        projection_x_end = self.camera_x.proj_scalar(vector_end - Vector3(self.camera_normal.start_pos))
        projection_x_start = self.camera_x.proj_scalar(vector_start - Vector3(self.camera_normal.start_pos))
        # same for this one but in the y direction
        # projection_y = self.camera_y.proj_scalar(vector - Vector3(self.camera_normal.start_pos))
        projection_y_end = self.camera_y.proj_scalar(vector_end - Vector3(self.camera_normal.start_pos))
        projection_y_start = self.camera_y.proj_scalar(vector_start - Vector3(self.camera_normal.start_pos))

        # the distance to the start of the vector
        distance_to_start = self.camera_normal.proj_scalar(vector_start - Vector3(self.camera_normal.start_pos))
        # the distance to the end of the vector
        distance_to_end = self.camera_normal.proj_scalar(vector_end - Vector3(self.camera_normal.start_pos))

        # print(f"{distance_to_start=}\n{distance_to_end=}")

        if distance_to_end <= 0 and distance_to_start <= 0:
            return

        # scaled start and end from the fov
        scaler_start = (math.tan(FOV/2) * distance_to_start) / 2 # seems to be off the divide by 2 is something
        scaler_end = (math.tan(FOV/2) * distance_to_end) / 2 # seems to be off

        # scaled to perspective
        perspective_x_start = projection_x_start / scaler_start
        perspective_x_end = projection_x_end / scaler_end
        
        perspective_y_start = projection_y_start / scaler_start
        perspective_y_end = projection_y_end / scaler_end

        # check if line passes edges of the screen
        edge_x_start = max(math.tan(FOV/2) * distance_to_start, 0)
        edge_y_start = max(math.tan(FOV/2) * distance_to_start * WINDOW_WIDTH/WINDOW_HEIGHT, 0) # scaled bc height is smaller
        
        edge_x_end = max(math.tan(FOV/2) * distance_to_end, 0)
        edge_y_end = max(math.tan(FOV/2) * distance_to_end * WINDOW_WIDTH/WINDOW_HEIGHT, 0) # scaled bc height is smaller

        if abs(projection_x_start) > abs(edge_x_start):
            projection_x_start = math.copysign(edge_x_start, projection_x_start)
        
        if abs(projection_y_start) > abs(edge_y_start):
            projection_y_start = math.copysign(edge_y_start, projection_y_start)
        
        if abs(projection_x_end) > abs(edge_x_end):
            projection_x_end = math.copysign(edge_x_end, projection_x_end)
        
        if abs(projection_y_end) > abs(edge_y_end):
            projection_y_end = math.copysign(edge_y_end, projection_y_end)


        draw_line_2d(surface, Vector2((perspective_x_end-perspective_x_start, perspective_y_end-perspective_y_start), (perspective_x_start, perspective_y_start), color=vector.color))


    def draw_vecs_3d(self, surface, vecs):
        for vec in vecs:
            self.draw_line_3d(surface, vec)


    def draw_vecs_1p(self, surface, vecs):
        for vec in vecs:
            self.one_point_perspective(surface, vec)