# -*- coding: utf-8 -*-

# Zugriff auf das Revit-Dokument und das pyRevit-Ausgabefenster
from pyrevit import revit, script

# Unsere eigenen Funktionen aus lib/raum_service.py importieren
from raum_service import raeume_sammeln, raumdaten_lesen

# Das aktuell geöffnete Revit-Modell abrufen
doc = revit.doc

# Das pyRevit-Ausgabefenster abrufen
ausgabe = script.get_output()

# Alle Raumelemente im Modell sammeln
raeume = raeume_sammeln(doc)

# Eine leere Liste für die Tabellenzeilen erstellen
zeilen = []

# Jeden gesammelten Raum einzeln durchgehen
for raum in raeume:
    # Geschoss, Nummer und Name lesen und als Tabellenzeile hinzufügen
    zeilen.append(raumdaten_lesen(raum, doc))

# Erst nach Geschossname, dann nach Raumnummer sortieren
# zeile[0] ist das Geschoss, zeile[1] ist die Raumnummer
zeilen.sort(key=lambda zeile: (zeile[0], zeile[1]))

# Die gesammelten Daten als Tabelle im Ausgabefenster anzeigen
ausgabe.print_table(
    table_data=zeilen,
    columns=["Geschoss", "Raumnummer", "Raumname"],
    title="Räume im Modell"
)