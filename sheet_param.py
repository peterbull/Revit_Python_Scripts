__title__ = ""
__author__ = "Peter Bull"

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

doc =  __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
sheets_collector = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Sheets)\
                                                    .WhereElementIsNotElementType()\
                                                    .ToElements()

t = Transaction(doc, "Update Sheet Parameters")
t.Start()

for sheet in sheets_collector:
    custom_param = sheet.LookupParameter('CUSTOM_PARAM')
    if custom_param:
        custom_param.Set("Example Value")

t.Commit()
