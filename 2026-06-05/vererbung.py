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

class Halbkugel(Kugel):
    def volumen(self):
        # return (2/3) * math.pi * self.radius**3
        return super().volumen() / 2
    @classmethod
    def from_volumen(cls, volumen):
        return super().from_volumen(volumen * 2)

hk = Halbkugel(5)
print("Volumen der Halbkugel:", hk.volumen())
hk2 = Halbkugel.from_volumen(260)
print("Radius der Halbkugel (aus Volumen):", hk2.radius)