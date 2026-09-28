import data
import os

def save():
    """Rewrite storage.py with current products and sales so everything persists after exit."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage.py")
    with open(path, "w") as f:
        f.write("products = {\n")
        for pid, p in data.products.items():
            f.write(f'    "{pid}": {{"name": "{p["name"]}", "price": {p["price"]}, "qty": {p["qty"]}}},\n')
        f.write("}\n\nsales = [\n")
        for s in data.sales:
            f.write(f"    {repr(s)},\n")
        f.write("]\n")
