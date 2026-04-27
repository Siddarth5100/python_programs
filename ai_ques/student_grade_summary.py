marks = {
    "Arun": 85,
    "Bala": 62,
    "Charu": 91,
    "Divya": 74,
    "Eshan": 58
}

result = {}

for key, value in marks.items():
    if not key in result:
        result[key] = ""
    

print(result)