# test_store.py
# Unit tests for the Store Management System
# Run: python tests/test_store.py

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import data


class TestInventory(unittest.TestCase):

    def setUp(self):
        data.products.clear()
        data.products.update({
            "P001": {"name": "Lays",    "price": 20, "qty": 50},
            "P002": {"name": "Pepsi",   "price": 40, "qty": 3},
            "P003": {"name": "Biscuit", "price": 10, "qty": 0},
        })
        data.sales.clear()

    def test_product_exists(self):
        self.assertIn("P001", data.products)

    def test_product_does_not_exist(self):
        self.assertNotIn("P999", data.products)

    def test_add_product(self):
        data.products["P010"] = {"name": "Juice", "price": 30, "qty": 20}
        self.assertIn("P010", data.products)
        self.assertEqual(data.products["P010"]["name"], "Juice")

    def test_delete_product(self):
        del data.products["P001"]
        self.assertNotIn("P001", data.products)

    def test_update_price(self):
        data.products["P001"]["price"] = 25
        self.assertEqual(data.products["P001"]["price"], 25)

    def test_update_quantity(self):
        data.products["P001"]["qty"] = 80
        self.assertEqual(data.products["P001"]["qty"], 80)

    def test_low_stock_detection(self):
        low = [pid for pid, p in data.products.items() if p["qty"] <= 5]
        self.assertIn("P002", low)
        self.assertIn("P003", low)
        self.assertNotIn("P001", low)

    def test_out_of_stock(self):
        out = [pid for pid, p in data.products.items() if p["qty"] == 0]
        self.assertIn("P003", out)

    def test_search_product(self):
        results = {pid: p for pid, p in data.products.items()
                   if "lay" in p["name"].lower()}
        self.assertIn("P001", results)


class TestBilling(unittest.TestCase):

    def setUp(self):
        data.products.clear()
        data.products.update({
            "P001": {"name": "Lays",  "price": 20, "qty": 50},
            "P002": {"name": "Pepsi", "price": 40, "qty": 10},
        })
        data.sales.clear()

    def test_bill_subtotal(self):
        cart = [
            {"id": "P001", "name": "Lays",  "price": 20, "qty": 3},
            {"id": "P002", "name": "Pepsi", "price": 40, "qty": 1},
        ]
        subtotal = sum(item["price"] * item["qty"] for item in cart)
        self.assertEqual(subtotal, 100)

    def test_bill_tax(self):
        subtotal = 100
        tax = round(subtotal * 0.05, 2)
        self.assertEqual(tax, 5.0)

    def test_bill_total(self):
        subtotal = 100
        tax   = round(subtotal * 0.05, 2)
        total = round(subtotal + tax, 2)
        self.assertEqual(total, 105.0)

    def test_stock_deduction(self):
        original = data.products["P001"]["qty"]
        data.products["P001"]["qty"] -= 5
        self.assertEqual(data.products["P001"]["qty"], original - 5)

    def test_sale_saved(self):
        data.sales.append({
            "customer": "Raj", "cart": [],
            "subtotal": 100, "tax": 5, "total": 105
        })
        self.assertEqual(len(data.sales), 1)
        self.assertEqual(data.sales[0]["total"], 105)


class TestReports(unittest.TestCase):

    def setUp(self):
        data.products.clear()
        data.products.update({
            "P001": {"name": "Lays", "price": 20, "qty": 40},
        })
        data.sales.clear()
        data.sales.extend([
            {"customer": "A", "cart": [{"id": "P001", "name": "Lays", "price": 20, "qty": 3}],
             "subtotal": 60, "tax": 3, "total": 63},
            {"customer": "B", "cart": [{"id": "P001", "name": "Lays", "price": 20, "qty": 2}],
             "subtotal": 40, "tax": 2, "total": 42},
        ])

    def test_total_revenue(self):
        total = sum(s["total"] for s in data.sales)
        self.assertEqual(total, 105)

    def test_total_bills(self):
        self.assertEqual(len(data.sales), 2)

    def test_top_selling_count(self):
        sold = {}
        for sale in data.sales:
            for item in sale["cart"]:
                pid = item["id"]
                sold[pid] = sold.get(pid, 0) + item["qty"]
        self.assertEqual(sold["P001"], 5)


if __name__ == "__main__":
    unittest.main()
