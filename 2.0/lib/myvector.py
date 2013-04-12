# -*- coding: utf-8 -*-

import math

class MyVector(object):
    """My class of Vector with methdos of vector operations"""
    def __init__(self, point):
        super(MyVector, self).__init__()
        self.x = point[0]
        self.y = point[1]
    
    def __add__(v1, v2):
        return MyVector((v1.x + v2.x, v1.y + v2.y))

    def __sub__(v1, v2):
        return MyVector((v1.x - v2.x, v1.y - v2.y))

    def __mul__(self, scalar):
        return MyVector((self.x * scalar, self.y * scalar))

    def __div__(self, scalar):
        return MyVector((self.x / scalar, self.y / scalar))

    def normalize(self):
        magnitude = self.get_magnitude()
        return MyVector((self.x / magnitude, self.y / magnitude))

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def totuple(self):
        return (self.x, self.y)

    def get_distance_to(self, v):
        return (self - v).get_magnitude()

def test():
    a = MyVector((0,4))
    b = MyVector((1,4))
    d = a.get_distance_to(b)
    print d

#test()

