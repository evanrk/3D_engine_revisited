from vectors import *
from functools import reduce

class Object3D:
    def __init__(self, face_vectors, vertices, faces):
        self.face_vectors = face_vectors
        self.vertices = vertices
        self.faces = faces

    @classmethod
    # read_obj is from gpt
    def read_obj(cls, filename):
        """creates a Object3d from the corresponding obj file"""
        vertices = []
        faces = []

        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue
                if parts[0] == 'v':  # This line is a vertex
                    vertex = list(map(float, parts[1:4]))  # Convert each part into a float
                    vertices.append(vertex)
                elif parts[0] == 'f':  # This line is a face
                    # Faces can be complex, but here we assume it's a simple face with vertex indices
                    face = [int(part.split('/')[0]) for part in parts[1:]]  # Convert indices to int
                    faces.append(face)


        face_vectors = []
        # faces are triangles in space (need 3 vectors each)
        for face in faces:
            face_vertices = [vertices[vertex_index-1] for vertex_index in face]
            
            # the last vector has index 2 as starting and index 0 as ending (easier to append first to the end)
            face_vertices.append(face_vertices[0])

            face_parts = []
            for first_vertex, second_vertex in zip(face_vertices[1:], face_vertices):
                face_vector = Vector3([b - a for a, b in zip(first_vertex, second_vertex)], first_vertex, color=(255, 255, 255))
                face_parts.append(face_vector)
            
            face_vectors.append(face_parts)    

        return cls(face_vectors, vertices, faces)

# Usage
# face_vectors, vertices, faces =
# Object3D.read_obj("cube.obj")
# print("Vertices:", vertices)
# print("Faces vecs:", face_vectors)