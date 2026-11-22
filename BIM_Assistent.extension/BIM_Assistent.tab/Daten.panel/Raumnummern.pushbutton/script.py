# -*- coding: utf-8 -*-
from pyrevit import DB, revit, forms

doc = revit.doc

raeume = (
    DB.FilteredElementCollector(doc)
    .OfCategory(DB.BuiltInCategory.OST_Rooms)
    .WhereElementIsNotElementType()
    .ToElements()
)

from pyrevit import script

ausgabe = script.get_output()
zeilen = []

for raum in raeume:
    nummer = raum.get_Parameter(
        DB.BuiltInParameter.ROOM_NUMBER
    ).AsString()

    name = raum.get_Parameter(
        DB.BuiltInParameter.ROOM_NAME
    ).AsString()

    ebene = doc.GetElement(raum.LevelId)
    geschoss = ebene.Name if ebene else "-"

    zeilen.append([geschoss, nummer, name])
    
zeilen.sort(key=lambda zeile: (zeile[0], zeile[1]))

ausgabe.print_table(
    table_data=zeilen,
    columns=["Geschoss", "Raumnummer", "Raumname"],
    title="Räume im Modell"
)