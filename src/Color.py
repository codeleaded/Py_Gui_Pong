
class Color:
    def __init__(self,r: float,g: float,b: float,a: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __init__(self,r: float,g: float,b: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = 1.0

    def get(self):
        return (int(self.r * 255.0),int(self.g * 255.0),int(self.b * 255.0))