import numpy as np
import math
class Vector2:
    def __init__(self, vec, start_pos=(0, 0)):
        self.values = np.array(vec)
        self.start_pos = start_pos
        self.end_pos = (start_pos[0] + vec[0], start_pos[1] + vec[1])


    @property
    def x(self):
        return self.values[0]

    @property
    def y(self):
        return self.values[1]
    
    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        """Adds vectors. Does not include starting position"""
        return Vector2(self.values + other.values)
    
    def __sub__(self, other):
        """Subtracts vectors. Does not include starting position"""
        return Vector2(self.values - other.values)

    def __mul__(self, other):
        """Multiplies vectors (either dot product or scalar multiplication). Does not include starting position"""
        if type(other) == Vector2:
            return Vector2(self.values.dot(other), start_pos=self.start_pos)
        elif isinstance(other, (int, float)):
            return Vector2(self.values * other)
        else:
            raise TypeError(f"Cannot multiply Vector2 and {type(other)}")

    def __rmul__(self, other):
        return other * self

    def __truediv__(self, other):
        """Divides vectors by a scalar (does not include starting position)"""
        return Vector2(self.values / other)

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return self.__str__()

    def proj(self, other):
        """returns the projected vector of other on self if self and other are touching. Does not include the starting position so you have to add it back in"""
        scalar = np.dot(self.values, other.values) / np.dot(self.values, self.values)
        return Vector2(scalar * self.values)

class Vector3:
    def __init__(self, vec, start_pos=(0, 0, 0)):
        self.values = np.array(vec)
        self.start_pos = start_pos

        self.end_pos = (start_pos[0] + vec[0], start_pos[1] + vec[1], start_pos[2] + vec[2])

    @property
    def x(self):
        return self.values[0]

    @property
    def y(self):
        return self.values[1]
    
    @property
    def z(self):
        return self.values[2]

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        """Adds vectors. Does not include starting position"""
        return Vector3(self.values + other.values)

    def __sub__(self, other):
        """Subtracts vectors. Does not include starting position"""
        return Vector3(self.values - other.values)

    def __mul__(self, other):
        """Multiplies vectors (either dot product or scalar multiplication). Does not include starting position"""
        if isinstance(other, Vector3):
            return Vector3(np.dot(self.values(other)))
        elif isinstance(other, (int, float)):
            return Vector3(self.values * other, start_pos=self.start_pos)
        else:
            raise TypeError(f"Cannot multiply Vector3 and {type(other)}")
    
    def __rmul__(self, other):
        return other * self

    def __truediv__(self, other):
        """Divides vectors by a scalar (does not include starting position)"""
        return Vector3(self.values / other)
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
        
    def __repr__(self):
        return self.__str__()
    
    
    def proj_scalar(self, other):
        """returns the scalar of the projected vector"""
        return np.dot(self.values, other.values) / np.dot(self.values, self.values)

    def proj(self, other):
        """returns the projected vector of other on self if self and other are touching. Does not include the starting position so you have to add it back in"""
        scalar = np.dot(self.values, other.values) / np.dot(self.values, self.values)
        return Vector3(scalar * self.values)
    

    def cross(self, other):
        """returns the cross product between this and another vector. Includes starting position of self"""
        return Vector3(np.cross(self.values, other.values), self.start_pos)