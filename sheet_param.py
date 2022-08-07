__title__ = ""
__author__ = "Peter Bull"

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, TransactionGroup

doc =  __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the sheets from the model
sheets_collector = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Sheets)\
                                                    .WhereElementIsNotElementType()\
                                                    .ToElements()

# Creating collector instance and collecting all wall element ids in the model
wall_id_collector = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Walls)\
                                                 .WhereElementIsNotElementType()\
                                                 .ToElementIds()

tg = TransactionGroup(doc, "Update and Delete")
tg.Start()

t = Transaction(doc, "Update Sheet Parameters")
t.Start()

for sheet in sheets_collector:
    custom_param = sheet.LookupParameter('CUSTOM_PARAM')
    if custom_param:
        custom_param.Set("Example Value")

t.Commit()




t = Transaction(doc, "Delete All Walls")

t.Start()

for wall_id in wall_id_collector:
    doc.Delete(wall_id)

t.Commit()

tg.Assimilate()
