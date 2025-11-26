import math

class Vf2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, v) -> any:
        return Vf2d(self.x + v.x, self.y + v.y)

    def __sub__(self, v) -> any:
        return Vf2d(self.x - v.x, self.y - v.y)

    def __mul__(self, v: float) -> any:
        return Vf2d(self.x * v, self.y * v)

    def __truediv__(self, v: float) -> any:
        return Vf2d(self.x / v, self.y / v)

    def __lt__(self, v) -> bool:
        return self.x < v.x and self.y < v.y

    def __gt__(self, v) -> bool:
        return self.x > v.x and self.y > v.y

    def dot(self, v) -> float:
        return self.x * v.x + self.y * v.y

    def mag(self) -> float:
        return math.sqrt(self.dot(self))

    def norm(self) -> any:
        return self / self.mag()
