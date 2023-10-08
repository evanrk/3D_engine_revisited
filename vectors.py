import numpy as np

class Vector2:
    def __init__(self, x, y):
        self.values = np.array([x, y])

    @property
    def x(self):
        return self.values[0]

    @property
    def y(self):
        return self.values[1]

    def __mul__(self, other):
        if type(other) == Vector2:
            return self.values.dot(other)
        if type(other) == int:
            return self.values * other
        
    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        print("hi!")
        return self.__str__


class Vector3:
    def __init__(self, x, y, z):
        self.values = np.array([x, y, z])

    @property
    def x(self):
        return self.values[0]

    @property
    def y(self):
        return self.values[1]
    
    @property
    def z(self):
        return self.values[2]

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return self.values.dot(other)
        elif isinstance(other, (int, float)):
            return self.values * other
        else:
            raise TypeError(f"Cannot multiply Vector3 and {type(other)}")
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
        
    def __repr__(self):
        return self.__str__()