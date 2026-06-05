import math
class Schneemann:
    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
    def volumen(self):
        v1 = (4/3) * math.pi * self.r1**3
        v2 = (4/3) * math.pi * self.r2**3
        v3 = (4/3) * math.pi * self.r3**3
        return v1 + v2 + v3

schneemann = Schneemann(3, 2, 1)
print("Volumen des Schneemanns:", schneemann.volumen())