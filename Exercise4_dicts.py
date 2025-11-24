inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 25,
    "Keyboard": 5,
    "Mouse": 12
}

inventory["Tablet"] = 10
inventory["Keyboard"] = 7

def low_stock(inv):
    return [p for p, q in inv.items() if q < 10]

print(low_stock(inventory))

del inventory["Mouse"]
print(inventory)

for product, qty in inventory.items():
    print(product, qty)
