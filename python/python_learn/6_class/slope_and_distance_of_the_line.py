#!/usr/bin/python3
import numpy as np
class Line(object):

    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2

    def distance(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return np.sqrt((x2-x1)**2 + (y2-y1)**2)

    def slope(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return (y2-y1)/(x2-x1)

coordinate1=(3,2)
coordinate2=(8,10)
li=Line(coordinate1,coordinate2)
print(f'The distance is {li.distance()}')
print(f'The slope is {li.slope()}')

