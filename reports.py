# reports.py
# Module 3 - Reports and Analytics
# Functions: sales summary, low stock alert, top selling products

import data

LOW_STOCK = 5


def sales_summary():
    print("\n========== SALES SUMMARY ==========")
    if not data.sales:
        print("No sales recorded yet.")
        return

    total_bills   = len(data.sales)
    total_revenue = sum(s["total"] for s in data.sales)
    total_tax     = sum(s["tax"]   for s in data.sales)

    print(f"Total Bills        : {total_bills}")
    print(f"Total Revenue      : Rs.{round(total_revenue, 2)}")
    print(f"Total Tax Collected: Rs.{round(total_tax, 2)}")


def low_stock_alert():
    print("\n========== LOW STOCK ALERT ==========")
    low_items = {pid: p for pid, p in data.products.items() if p["qty"] <= LOW_STOCK}
    if not low_items:
        print("All products are well stocked.")
        return
    print(f"{'ID':<8} {'Name':<20} {'Stock'}")
    print("-" * 35)
    for pid, p in low_items.items():
        status = "OUT OF STOCK" if p["qty"] == 0 else str(p["qty"]) + " left"
        print(f"{pid:<8} {p['name']:<20} {status}")


def top_selling():
    print("\n========== TOP SELLING PRODUCTS ==========")
    if not data.sales:
        print("No sales data yet.")
        return

    sold = {}
    for sale in data.sales:
        for item in sale["cart"]:
            pid = item["id"]
            if pid not in sold:
                sold[pid] = {"name": item["name"], "qty": 0, "revenue": 0}
            sold[pid]["qty"]     += item["qty"]
            sold[pid]["revenue"] += item["price"] * item["qty"]

    ranked = sorted(sold.items(), key=lambda x: x[1]["qty"], reverse=True)

    print(f"{'Product':<20} {'Units Sold':<12} {'Revenue'}")
    print("-" * 45)
    for pid, info in ranked:
        print(f"{info['name']:<20} {info['qty']:<12} Rs.{info['revenue']}")
