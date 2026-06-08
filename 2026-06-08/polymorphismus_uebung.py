from math import pi, sqrt

class Kreis:
    def __init__(self, radius):
        self.radius = radius
    def flaeche(self):
        return pi * self.radius**2
    def umfang(self):
        return 2 * pi * self.radius
class Rechteck:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def flaeche(self):
        return self.a * self.b
    def umfang(self):
        return 2 * (self.a + self.b)
class Quadrat(Rechteck):
    def __init__(self, a):
        super().__init__(a, a)
class Dreieck:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def umfang(self):
        return self.a + self.b + self.c
    def flaeche(self):
        u_halbe = self.umfang() / 2
        return sqrt(u_halbe * (u_halbe - self.a) * (u_halbe - self.b) * (u_halbe - self.c))
class GleichseitigesDreieck(Dreieck):
    def __init__(self, a):
        super().__init__(a, a, a)
class RechtwinkligesDreieck(Dreieck):
    def __init__(self, a, b):
        c = sqrt(a**2 + b**2)
        super().__init__(a, b, c)

k = Kreis(10)
print(f"Kreis: A={k.flaeche()}; U={k.umfang()}")
r = Rechteck(10, 20)
print(f"Rechteck: A={r.flaeche()}; U={r.umfang()}")
q = Quadrat(10)
print(f"Quadrat: A={q.flaeche()}; U={q.umfang()}")
d = Dreieck(3, 4, 5)
print(f"Dreieck: A={d.flaeche()}; U={d.umfang()}")
g = GleichseitigesDreieck(10)
print(f"Gleichseitiges Dreieck: A={g.flaeche()}; U={g.umfang()}")
rt = RechtwinkligesDreieck(3, 4)
print(f"Rechtwinkliges Dreieck: A={rt.flaeche()}; U={rt.umfang()}")

formen = [
    Kreis(10),
    Rechteck(10, 20),
    Quadrat(10),
    Dreieck(3, 4, 5),
    GleichseitigesDreieck(10),
    RechtwinkligesDreieck(3, 4)
]
for form in formen:
    print(f"{form.__class__.__name__}: A={form.flaeche()}; U={form.umfang()}")