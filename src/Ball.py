from Vf2d import *
from Rect import *
from Color import *

class Ball(Rect):
    def __init__(self,x: float,y: float,r: float,c: Color):
        super().__init__(x,y,r * 2.0,r * 2.0,0.0,0.0,c)

    # returns position of scoring player, 0 in case of no goal
    def goal(self,screen :Vf2d):
        if(self.p.x < 0.0):
            return 1
        elif(self.p.x + self.d.x > screen.x):
            return 2
        else:
            return 0