class Circle():

    PI = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.PI * 2

    def get_area(self):
        return self.radius * self.radius * Circle.PI
    
c = Circle(30)
print(c.get_circumference())
print(c.get_area())
