class Adresse:
    def __init__(self, name, strasse, plz, ort):
        self.name = name
        self.strasse = strasse
        self.plz = plz
        self.ort = ort

    def briefadresse(self):
        briefadresse = f"{self.name}\n"
        briefadresse += f"{self.strasse}\n"
        briefadresse += f"{self.plz} {self.ort}"
        return briefadresse

adr = Adresse(
    name = "Max Mustermann",
    strasse = "Lohrtalweg 10",
    plz = "74821",
    ort = "Mosbach"
)
print(adr.briefadresse())