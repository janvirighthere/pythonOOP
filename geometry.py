from math import sqrt, pi
class Line():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
    
        dist = sqrt((x2 - x1)** 2 + (y2 - y1)**2)
        return dist

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 -y1)/(x2 -x1)
      
class Cylinder():

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return round(pi * self.radius**2 * self.height, 2)

    def area(self):
        return round((2*pi*self.radius*self.height) + (2*pi*self.radius**2), 2)


