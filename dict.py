def top_note(student):
    return {"name": student["name"], "top_note": max(student["note"])}

print(top_note({"name": "John", "top_note" : [5,6,7]}))