"""
Advanced Collection of Data: Collects walls using "WherePasses" instead
of iterating over entire DB
"""

# for timing----------------------------------------------
from pyrevit.coreutils import Timer
timer = Timer()
#----------------------------------------------------------

import Autodesk.Revit.DB as DB

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def get_tall_walls(wall_height):
    height_param_id = DB.ElementId(DB.BuiltInParameter.WALL_USER_HEIGHT_PARAM)

    height_param_prov = DB.ParameterValueProvider(height_param_id)

    param_equality = DB.FilterNumericEquals()

    height_value_rule = DB.FilterDoubleRule(height_param_prov,
                                            param_equality,
                                            wall_height,
                                            1E-6)

    param_filter = DB.ElementParameterFilter(height_value_rule)

    walls = DB.FilteredElementCollector(doc) \
              .WherePasses(param_filter) \
              .ToElementIds()
    return walls

# uidoc.Selection.SetElementIds(walls)

# for timing----------------------------------------------
end_time = timer.get_time()
print(endtime)
#----------------------------------------------------------

# print(height_param_id)
# print(height_param_prov)
# print(param_equality)
# print(height_value_rule)
# print(param_filter)
# print(walls)
