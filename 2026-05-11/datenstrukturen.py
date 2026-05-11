## list
folge1 = [10,20,30]
# Reihenfolge der Elemente ist wichtig
folge2 = [10,30,20]
print(folge1)
print(folge2)
# Zugiff über Index
print(folge1[0])
print(folge1[1])
print(folge1[2])
# Veränderbar, doppelte Werte erlaubt
folge2[1] = 42
print(folge2)
#folge2[3] = 42
folge2.append(42)
print(folge2)
# Verwendung in For Schleifen
for element in folge1:
    print(element)
for i, n in enumerate(folge1):
    # Insbesondere bei schreibenen Zugriffen auf lists
    print(i, n)
for i in range(5):
    print(i)
for i in range(12, 17):
    print(i)
for i in range(20, 30, 2):
    print(i)
# Mischung von Typen möglich, aber nicht empfohlen
print([42, "Hello World", True])

## dict
person = { "name": "Max", "alter": 25 }
# Zugriff über Schlüssel
print(person["name"])
# Veränderbar
person["alter"] = 26
# Schlüssel sind eindeutig
person2 = { "name": "Max", "alter": 25, "name": "Moritz" }
print(person2)
# Verwendung in For Schleifen
for key in person:
    print(key, person[key])
for key, value in person.items():
    print(key, value)

## Kombination aus list und dict
personen = [
    { "name": "Max", "alter": 25 },
    {
        "name": "Moritz",
        "alter": 26
    }
]
print(personen)
print(personen[0])
print(personen[0]["name"])

zahlen = {
    "gerade": [0, 2, 4, 6, 8],
    "ungerade": [1, 3, 5, 7, 9]
}

## set
zahlen1 = {1, 2, 3}
zahlen2 = {1, 2, 3, 1}
print(zahlen1)
print(zahlen2)
# ohne Reihenfolge
zahlen3 = {3, 2, 1}
print(zahlen3)
# Veränderbar
zahlen1.add(4)
print(zahlen1)
# Mengenlogik
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) # Schnittmenge
print(a | b) # Vereinigung
# Verwendung in For Schleifen
for element in zahlen1:
    print(element)

## tuple
p1 = (1,2)
p2 = (2,1)
print(p1)
print(p2)
print(p1[0])
# Nicht veränderbar
#p1[0] = 42
# Verwendung auch ohne Klammern bei mehreren Rückgabewerten von Funktionen
def swap(a, b):
    return b, a
x, y = swap(1, 2)
print(x, y)
# Verwendung in For Schleifen
punkte = [(1,2), (3,4), (5,6)]
for x, y in punkte:
    print(x, y)