import testpaket.testmodul
# importiert alle Klassen und Funktionen aus testpaket/testmodul.py
t = testpaket.testmodul.Testklasse()

from testpaket import testmodul
# importiert das Modul testmodul aber unter dem Namen testmodul
t = testmodul.Testklasse()

from testpaket.testmodul import Testklasse
# importiert die Klasse Testklasse direkt in den aktuellen Namensraum
t = Testklasse()

import testpaket
# sieht gut aus, tut in dem Fall aber nichts