
import math

class Vector2:

    def __init__(self,x,y):

        self.x=x
        self.y=y


    def dlzka(self):

        return math.sqrt(self.x*self.x+self.y*self.y)

    def __add__(self,other):

        return Vector2(self.x+other.x,self.y+other.y)

    def __repr__(self):

        return f'Vector2({self.x},{self.y})'


