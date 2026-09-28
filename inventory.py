# inventory.py
# Module 1 - Inventory Management
# Functions: view, add, update, delete, search products

import data
from save import save

LOW_STOCK = 5


def view_products():
    print("\n========== INVENTORY ==========")
    if not data.products:
        print("No products found.")
        return
    print(f"{'ID':<8} {'Name':<20} {'Price':<12} {'Stock'}")
    print("-" * 48)
    for pid, p in data.products.items():
        note = " << LOW STOCK" if p["qty"] <= LOW_STOCK else ""
        print(f"{pid:<8} {p['name']:<20} Rs.{p['price']:<9} {p['qty']}{note}")
    print(f"\nTotal products: {len(data.products)}")


def add_product():
    print("\n========== ADD PRODUCT ==========")
    pid = input("Enter Product ID (e.g. P006): ").strip().upper()
    if not pid:
        print("ERROR: ID cannot be empty.")
        return
    if pid in data.products:
        print("ERROR: Product ID already exists.")
        return
    name = input("Enter Product Name: ").strip()
    if not name:
        print("ERROR: Name cannot be empty.")
        return
    try:
        price = int(input("Enter Price (Rs.): "))
        qty   = int(input("Enter Stock Quantity: "))
    except ValueError:
        print("ERROR: Price and quantity must be numbers.")
        return
    if price < 0 or qty < 0:
        print("ERROR: Values cannot be negative.")
        return
    data.products[pid] = {"name": name, "price": price, "qty": qty}
    save()
    print(f"SUCCESS: '{name}' added with ID {pid}.")


def update_product():
    print("\n========== UPDATE PRODUCT ==========")
    pid = input("Enter Product ID to update: ").strip().upper()
    if pid not in data.products:
        print("ERROR: Product not found.")
        return
    p = data.products[pid]
    print(f"Current -> Name: {p['name']} | Price: Rs.{p['price']} | Stock: {p['qty']}")
    try:
        p["price"] = int(input("New Price (Rs.): "))
        p["qty"]   = int(input("New Stock Quantity: "))
    except ValueError:
        print("ERROR: Must be a number.")
        return
    save()
    print("SUCCESS: Product updated.")


def delete_product():
    print("\n========== DELETE PRODUCT ==========")
    pid = input("Enter Product ID to delete: ").strip().upper()
    if pid not in data.products:
        print("ERROR: Product not found.")
        return
    name = data.products[pid]["name"]
    confirm = input(f"Delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del data.products[pid]
        save()
        print(f"SUCCESS: '{name}' deleted.")
    else:
        print("Cancelled.")


def search_product():
    print("\n========== SEARCH PRODUCT ==========")
    keyword = input("Enter name to search: ").strip().lower()
    results = {pid: p for pid, p in data.products.items()
               if keyword in p["name"].lower()}
    if not results:
        print(f"No products found matching '{keyword}'.")
        return
    print(f"{'ID':<8} {'Name':<20} {'Price':<12} {'Stock'}")
    print("-" * 48)
    for pid, p in results.items():
        print(f"{pid:<8} {p['name']:<20} Rs.{p['price']:<9} {p['qty']}")
