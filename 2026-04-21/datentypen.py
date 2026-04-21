v1 = None
v2 = True
v3 = 42
v4 = 3.14
v5 = 4.3e5
v6 = 1+4j
v7 = "Hallo', Welt!"
v8 = 'Hallo", Welt!'
v9 = "Hallo\nWelt!"

v = 42
print(v)
print(type(v))
v = "42"
print(v)
print(type(v))

## Explizite Typkonvertierung
# int()
print(int(3.14))
print(int(2.99))
print(int("12"))
#print(int("12.34"))  # Fehler: ungültige Literale für int()
print(int(True))  # True wird zu 1
print(int(False)) # False wird zu 0

# float()
print(42)
print(float(42))
print(float("3"))

# str()
print(type(42))
print(type(str(42)))