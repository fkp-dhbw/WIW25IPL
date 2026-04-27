print("5 / 2 =", 5 // 2, "Rest:", 5 % 2)
print(type(4/3))
print(type(4/2))
print(type(4//2))
print(True + True)
print("Hallo " + "Welt")

# Zuweisungsoperatoren
x = 5
x = x + 3
x += 3
a, b = 1, 2

# Logische Operatoren
print(0 < x and x < 10)
print(0 < x < 10)

# Weitere
alter = 12
volljaehrig = alter >= 18
if volljaehrig:
    print("Du bist volljährig.")
if volljaehrig := alter >= 18:
    print("Du bist volljährig.")
print("ipsum" in "Lorem ipsum dolor sit amet")
a = "Test"
b = "Te"
b += "st"
print(id(a), id(b))
print(a is b)
print(a == b)