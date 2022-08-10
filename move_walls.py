"""
Advanced collection of data: Collect all the walls at height of 10
by iterating over all walls in project and checking parameter
"""

from System.Collections.Generic import List
import Autodesk.Revit.DB as DB
from pyrevit import revit, DB

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

wall_id_collector = DB.FilteredElementCollector(doc) \
                      .OfCategory(DB.BuiltInCategory.OST_Walls) \
                      .WhereElementIsNotElementType() \
                      .ToElements()


rotation = 45.0

for wall in wall_id_collector:
    wall_origin = wall.Location.Point
    line_z = Line.CreateBound(wall_origin, XYZ(wall_origin.X, wall_origin.Y, wall_origin.Z +1))
    ElementTransformUtils.RotateElement(doc, wall.Id, line_z, rotation)


# t = Transaction(doc, "Move Walls Left")
# t.Start()

# for wall in walls:
