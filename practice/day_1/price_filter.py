products = {
    "Pen": 12,
    "Notebook": 40,
    "Eraser": 8,
    "Bag": 550
}


for key, val in products.items():
    if val > 20:
        print(key)