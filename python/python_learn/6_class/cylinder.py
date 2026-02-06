#!/usr/bin/python3
class Cylinder:
    height=1
    radius=1
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.height*3.14*(self.radius)**2

    def surface_area(self):
        top=3.14*(self.radius)**2
        return (2*top)+ 2*(3.14*self.radius*self.height)

c=Cylinder(2,3)
print(c.volume())
print(c.surface_area())
