#!/usr/bin/env python3
# Kommentar
a = "Test" # Kommentar
'''
Mehrzeiliger
Kommentar
'''

p = 42
if p > 90:
    print("Sehr gut!")
elif p > 50:
    print("Bestanden")
else:
    print("Leider nicht bestanden.")

# geschachtelte Bedinungungen
if p > 50:
    print("Bestanden")
    if p > 90:
        print("Sehr gut!")
else:
    print("Leider nicht bestanden.")

# Inline (nur bei einer Anweisung)
if p > 50:
    print("Bestanden")
    if p > 90: print("Sehr gut!")
else: print("Leider nicht bestanden.")

if p > 50:
	print("Test")
    #print("Test2")

month = 4
match month:
    case 2:
        days = 28
    case 4 | 6 | 9 | 11:
        days = 30
    case _:
        days = 31

x = 1
while x < 100:
    print("Verdopple x =", x)
    x *= 2
print("Nun ist x =", x)

for c in "Hello World":
    print("Zeichen: ", c)

i = 0
while True:
    print("Endlosschleife, i =", i)
    i += 1
    if i > 10: break

i = 0
while i < 10:
    i += 1
    if i % 2 == 0: continue
    print("Ungerader Wert:", i)


import math
print(math.sqrt(16))
print(int(math.sqrt(16)))
from math import sqrt as wurzel
print(wurzel(16))