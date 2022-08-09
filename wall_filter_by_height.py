"""
Advanced collection of data: Collect all the walls at height of 10
by iterating over all walls in project and checking parameter
"""

from System.Collections.Generic import List

import Autodesk.Revit.DB as DB

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

walls = DB.FilteredElementCollector(doc) \
        .OfCategory(DB.BuiltInCategory.OST_Walls) \
        .WhereElementIsNotElementType() \
        .ToElements()

tallwalls_ids = []

for wall in walls:
    heightp = wall.LookupParameter('Unconnected Height')
    if heightp and heightp.AsDouble() == 10.0:
        tallwalls_ids.append(wall.Id)

uidoc.Selection.SetElementIds(List[DB.ElementId](tallwalls_ids))
