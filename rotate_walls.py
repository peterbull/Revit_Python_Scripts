"""
Testing transactions and geometry manipulation with pyrevit/Revit API
"""

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from Autodesk.Revit.DB import Line, XYZ, Location, ElementTransformUtils
from pyrevit import revit, DB

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# collect all walls as elements in current model
wall_id_collector = FilteredElementCollector(doc) \
                    .OfCategory(DB.BuiltInCategory.OST_Walls) \
                    .WhereElementIsNotElementType() \
                    .ToElements()

# provide degrees to rotate as double
rotation = 45.0

#begin transaction
t = Transaction(doc, "Rotate Walls 45")
t.Start()

#iterate over walls, draw axis line 1 unit in z direction, rotate element on axis
for wall in wall_id_collector:
    wall_origin = wall.Location
    xyz_origin = wall_origin.Curve.GetEndPoint(0)
    line_z = Line.CreateBound(xyz_origin, XYZ(xyz_origin.X, xyz_origin.Y, xyz_origin.Z +1))
    ElementTransformUtils.RotateElement(doc, wall.Id, line_z, rotation)


t.Commit()
