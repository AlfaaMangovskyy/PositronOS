from math import sin, cos

class Point:
    def __init__(self, x : int, y : int, z : int):
        self.x = x
        self.y = y
        self.z = z
        self.rx = 0
        self.ry = 0
        self.rz = 0

    def rotateX(self, angle : float):
        self.rx += angle
        while self.rx > 360:
            self.rx -= 360

    def rotateY(self, angle : float):
        self.ry += angle
        while self.ry > 360:
            self.ry -= 360

    def rotateZ(self, angle : float):
        self.rz += angle
        while self.rz > 360:
            self.rz -= 360

    def getRotated(self):
        return (
            self.x * cos(self.rx) + self.z * sin(self.rx)
        )