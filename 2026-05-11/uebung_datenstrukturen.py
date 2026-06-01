def tisch_schach():
  print("=== Tisch 1: Schach ===")
  dame_weiss = (1, 4)
  dame_schwarz = (8, 4)
  print("Weiße Dame:", dame_weiss)
  print("Schwarze Dame:", dame_schwarz)
  print()

def tisch_blackjack():
  print("=== Tisch 2: Black Jack ===")
  karten = [10, 7, 5]
  karten.append(2)
  summe = sum(karten)
  print("Karten:")
  for karte in karten:
    print(karte)
  print("Summe:", summe)
  print()

def tisch_lotto():
  print("=== Tisch 3: Lotto ===")
  zahlen_liste = [3, 7, 28, 12, 19, 3]
  zahlen_set = set(zahlen_liste)
  print("Gezogene Zahlen (ohne Duplikate):")
  for zahl in sorted(zahlen_set):
    print(zahl)
  print()

def tisch_schiffe():
  print("=== Tisch 4: Schiffe versenken ===")
  schiff = {
    "x": 3,
    "y": 5,
    "richtung": "horizontal",
    "groesse": 4
  }
  print("Schiff:")
  print(schiff)
  print("\nSpielfeld:")
  for i in range(1, 11):
    for j in range(1, 11):
      if schiff["richtung"] == "horizontal":
        if i == schiff["x"] and schiff["y"] <= j < schiff["y"] + schiff["groesse"]:
          print("X", end=" ")
          # https://docs.python.org/3/library/functions.html#print
        else:
          print("0", end=" ")
      else:
        if j == schiff["y"] and schiff["x"] <= i < schiff["x"] + schiff["groesse"]:
          print("X", end=" ")
        else:
          print("0", end=" ")
    print()
  print()

tisch_schach()
tisch_blackjack()
tisch_lotto()
tisch_schiffe()