class Tour:
    def __init__(self, strecke, zeit_in_stunden):
        if strecke < 0:
            raise ValueError("Die Strecke darf nicht negativ sein.")
        self.strecke = strecke
        self.zeit_in_stunden = zeit_in_stunden
    def durchschnittsgeschwindigkeit(self):
        return self.strecke / self.zeit_in_stunden

tourbuch = []
try:
    tourbuch.append(Tour(30, 1.5))
    tourbuch.append(Tour(40, 2))
    tourbuch.append(Tour(60, 3.5))
    tourbuch.append(Tour(-20, 1))
    tourbuch.append(Tour(50, 0))
except ValueError as e:
    print(e)

try:
    for tour in tourbuch:
        print(f"Strecke: {tour.strecke} km, Zeit: {tour.zeit_in_stunden} h, Durchschnittsgeschwindigkeit: {tour.durchschnittsgeschwindigkeit()} km/h")
    print("Alle Touren wurden erfolgreich berechnet.")
except Exception as e:
    print(f"Fehler: {e}")