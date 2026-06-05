import math

class Kugel:
    def __init__(self, radius):
        self.radius = radius
    def volumen(self):
        return (4/3) * math.pi * self.radius**3

class Schneemann:
    def __init__(self, r1, r2, r3):
        self.kugel1 = Kugel(r1)
        self.kugel2 = Kugel(r2)
        self.kugel3 = Kugel(r3)
    def volumen(self):
        return (
            self.kugel1.volumen() +
            self.kugel2.volumen() +
            self.kugel3.volumen()
        )

kugeln = [Kugel(3), Kugel(2), Kugel(1)]
gesamt = 0
for kugel in kugeln:
    gesamt += kugel.volumen()
print("Gesamtvolumen der Kugeln:", gesamt)

schneemaenner = {
    "klein": Schneemann(1, 0.5, 0.25),
    "gross": Schneemann(3, 2, 1)
}
print("Volumen des kleinen Schneemanns:", schneemaenner["klein"].volumen())