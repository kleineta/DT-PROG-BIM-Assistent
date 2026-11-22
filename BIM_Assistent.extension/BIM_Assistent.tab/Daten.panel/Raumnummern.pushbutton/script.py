# -*- coding: utf-8 -*-

# Zugriff auf das aktuelle Revit-Modell und das Ausgabefenster
from pyrevit import revit, script

# Unsere eigenen Funktionen aus raum_service.py importieren
from raum_service import (
    raeume_sammeln,
    raumdaten_lesen,
    raumnummer_vorschlagen
)

# Das aktuell geöffnete Modell und das Ausgabefenster abrufen
doc = revit.doc
ausgabe = script.get_output()

# Alle Raumelemente sammeln
raeume = raeume_sammeln(doc)

# Eine leere Liste für die Vorschautabelle erstellen
zeilen = []

# Jeden Raum einzeln bearbeiten
for raum in raeume:

    # Geschoss, bisherige Nummer und Raumname lesen
    geschoss, nummer, name = raumdaten_lesen(raum, doc)

    # Eine neue Raumnummer vorschlagen
    vorschlag = raumnummer_vorschlagen(geschoss, nummer)

    # Räume ohne Vorschlag zur weiteren Prüfung markieren
    if vorschlag is None:
        vorschlag = u"Noch zu klären"

    # Die Werte als Zeile zur Vorschautabelle hinzufügen
    zeilen.append([geschoss, nummer, vorschlag, name])

# Nach Geschossname und bisheriger Raumnummer sortieren
# Fehlende Werte beim Sortieren wie leeren Text behandeln
zeilen.sort(key=lambda zeile: (zeile[0] or "", zeile[1] or ""))

# Alte und vorgeschlagene Nummern nebeneinander anzeigen
ausgabe.print_table(
    table_data=zeilen,
    columns=[
        "Geschoss",
        "Bisherige Nummer",
        "Vorgeschlagene Nummer",
        "Raumname"
    ],
    title=u"Vorschau der Raumnummerierung"
)