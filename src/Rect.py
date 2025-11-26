from Vf2d import *
from Rect import *
from Color import *

class Rect:
    def __init__(self, x: float, y: float, w: float, h: float, vx: float, vy: float, c: Color):
        self.p = Vf2d(x,y)
        self.d = Vf2d(w,h)
        self.v = Vf2d(vx,vy)
        self.c = c

    def update(self, t: float):
        self.p += self.v * t

    def collision_border(self,border): # border: Rect
        #if self.p.x < border.p.x:
        #    self.p.x = border.p.x
        #elif self.p.x > border.p.x + border.d.x - self.d.x:
        #    self.p.x = border.p.x + border.d.x - self.d.x
        if self.p.y < border.p.y:
            self.p.y = border.p.y
            self.v.y *= -1.0
        elif self.p.y > border.p.y + border.d.y - self.d.y:
            self.p.y = border.p.y + border.d.y - self.d.y
            self.v.y *= -1.0

    def collision(self,r): # r: Rect | other Rect -> Ball
        if self.overlap(r):
            r.v.x *= -1.0
            r.v = r.v.norm() * (r.v.mag() + 100.0)
    
    def overlap(self,r): # r: Rects
        return self.p < r.p + r.d and self.p + self.d > r.p  
    

