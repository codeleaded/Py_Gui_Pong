from Vf2d import *
from Rect import *
from Color import *

class Paddle(Rect):
    def __init__(self,x: float,y: float,w: float,h: float,c: Color):
        super().__init__(x,y,w,h,0.0,0.0,c)
        self.points = 0

    def move(self,vy: float):
        self.v.y = vy