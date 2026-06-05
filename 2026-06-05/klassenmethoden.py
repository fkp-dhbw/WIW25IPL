import math

class Kugel:
    def __init__(self, radius):
        self.radius = radius
    def volumen(self):
        return (4/3) * math.pi * self.radius**3
    @classmethod
    def from_volumen(cls, volumen):
        radius = ((3 * volumen) / (4 * math.pi)) ** (1/3)
        return cls(radius)

k1 = Kugel(3)
print("Volumen der Kugel:", k1.volumen())
k2 = Kugel.from_volumen(100)
print("Radius der Kugel mit Volumen 100:", k2.radius)