# billing.py
# Module 2 - Billing System
# Functions: create bill, view recent bills

import data
from save import save

TAX_RATE = 0.05  # 5% GST


def create_bill():
    print("\n========== CREATE BILL ==========")
    customer = input("Customer Name (press Enter to skip): ").strip()
    if not customer:
        customer = "Walk-in Customer"

    cart = []

    while True:
        print("\nCurrent cart items:", len(cart))
        pid = input("Enter Product ID to add (or 'done' to finish): ").strip().upper()

        if pid == "DONE":
            if len(cart) == 0:
                print("Cart is empty. Add at least one item.")
                continue
            break

        if pid not in data.products:
            print("ERROR: Product not found. Try again.")
            continue

        p = data.products[pid]
        if p["qty"] == 0:
            print(f"ERROR: '{p['name']}' is out of stock.")
            continue

        print(f"  {p['name']} | Price: Rs.{p['price']} | Available: {p['qty']}")

        try:
            qty = int(input("  Enter quantity: "))
        except ValueError:
            print("ERROR: Enter a valid number.")
            continue

        if qty <= 0:
            print("ERROR: Quantity must be at least 1.")
            continue

        if qty > p["qty"]:
            print(f"ERROR: Only {p['qty']} units available.")
            continue

        found = False
        for item in cart:
            if item["id"] == pid:
                item["qty"] += qty
                found = True
                print(f"  Updated quantity to {item['qty']}.")
                break

        if not found:
            cart.append({"id": pid, "name": p["name"], "price": p["price"], "qty": qty})
            print(f"  Added to cart.")

        data.products[pid]["qty"] -= qty

    subtotal = sum(item["price"] * item["qty"] for item in cart)
    tax      = round(subtotal * TAX_RATE, 2)
    total    = round(subtotal + tax, 2)

    print("\n" + "=" * 40)
    print("       STORE MANAGEMENT SYSTEM")
    print("            BILL RECEIPT")
    print("=" * 40)
    print(f"Customer : {customer}")
    print("-" * 40)
    print(f"{'Item':<20} {'Qty':<6} {'Amount'}")
    print("-" * 40)
    for item in cart:
        amount = item["price"] * item["qty"]
        print(f"{item['name']:<20} {item['qty']:<6} Rs.{amount}")
    print("-" * 40)
    print(f"{'Subtotal':<30} Rs.{subtotal}")
    print(f"{'Tax (5%)':<30} Rs.{tax}")
    print(f"{'TOTAL':<30} Rs.{total}")
    print("=" * 40)

    data.sales.append({
        "customer": customer,
        "cart":     cart,
        "subtotal": subtotal,
        "tax":      tax,
        "total":    total
    })
    save()
    print("Bill saved successfully.\n")


def view_bills():
    print("\n========== RECENT BILLS ==========")
    if not data.sales:
        print("No bills recorded yet.")
        return
    recent = data.sales[-5:]
    for i, sale in enumerate(reversed(recent), 1):
        print(f"\n  Bill #{i}")
        print(f"  Customer : {sale['customer']}")
        print(f"  Items    : {len(sale['cart'])}")
        print(f"  Total    : Rs.{sale['total']}")
