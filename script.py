# -*- coding: utf-8 -*-
__title__ = "Optimize\nModel Health"
__author__ = "ALBE Studio"

from pyrevit import revit, DB, forms

doc = revit.doc

def delete_unplaced_rooms():
    # Collect all rooms
    rooms = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Rooms).ToElements()
    
    unplaced_rooms = []
    for room in rooms:
        # Check if room is unplaced, unclosed, or redundant
        if room.Area == 0 or room.Location is None:
            unplaced_rooms.append(room.Id)
            
    if unplaced_rooms:
        with revit.Transaction("Purge Unplaced Rooms"):
            for room_id in unplaced_rooms:
                doc.Delete(room_id)
        return len(unplaced_rooms)
    return 0

# Execute the cleanup
deleted_count = delete_unplaced_rooms()

if deleted_count > 0:
    forms.alert("Model Optimized!\nSuccessfully deleted {} unplaced/redundant rooms.".format(deleted_count), title="ALBE BIM Tools")
else:
    forms.alert("Model is clean! No unplaced rooms found.", title="ALBE BIM Tools")
