# Store Management System

A command-line Store Management System built in Python for the Python Essentials course project at VIT Bhopal University.

---

## Overview

A simple terminal-based tool for managing a small store's products, billing, and sales reports. Built using only Python's standard library — no external packages, no files, no database. All data is stored in Python dictionaries and lists during the session.

---

## Features

**Module 1 – Inventory Management**
- View all products (with low stock warnings)
- Add new products
- Update price and quantity
- Delete products
- Search by name

**Module 2 – Billing System**
- Create itemised customer bills
- Automatic 5% GST tax calculation
- Stock auto-deducted on billing
- View last 5 bills

**Module 3 – Reports & Analytics**
- Sales summary (total revenue, total bills, tax collected)
- Low stock alert (flags items with 5 or fewer units)
- Top selling products by quantity sold

---

## Technologies Used

- Python 3.x (standard library only)
- Data stored using Python dictionaries and lists (no files, no database)
- `unittest` module for automated testing

---

## Project Structure

```
store-management/
├── main.py           # Entry point – runs the menu
├── storage.py        # Single source of truth for all data
├── data.py           # Re-exports from storage (shared references)
├── inventory.py      # Module 1 – Inventory management
├── billing.py        # Module 2 – Billing system
├── reports.py        # Module 3 – Reports & analytics
├── tests/
│   └── test_store.py # 17 unit tests
├── README.md
└── statement.md
```

---

## Requirements

- Python 3.6 or above
- No external packages needed — standard library only

---

## How to Run

**Step 1 – Clone the repository**
```bash
git clone https://github.com/{your-username}/store-management
cd store-management
```

**Step 2 – Run the application**
```bash
python main.py
```

**Step 3 – Use the menu**
```
---------- MAIN MENU ----------
 1. View All Products
 2. Add Product
 3. Update Product
 4. Delete Product
 5. Search Product
 6. Create Bill
 7. View Recent Bills
 8. Sales Summary
 9. Low Stock Alert
10. Top Selling Products
 0. Exit
```

---

## Running Tests

```bash
python tests/test_store.py
```

Expected output:
```
Ran 17 tests in 0.001s
OK
```

---

## Usage Guide

1. Run `python main.py`
2. Start with **Option 1** to see the 5 pre-loaded products
3. Use **Option 2** to add a new product — it will appear immediately in inventory
4. Use **Option 6** to create a bill — stock is deducted automatically
5. Use **Options 8–10** to view reports and alerts

---

## Non-Functional Requirements

| Requirement       | Implementation                                              |
|-------------------|-------------------------------------------------------------|
| Performance       | All operations are O(1) or O(n) dictionary/list lookups    |
| Usability         | Clear numbered menu, descriptive prompts, error messages    |
| Reliability       | Input validation on all fields; graceful error handling     |
| Maintainability   | Modular design — 6 separate files, single responsibility    |
| Error Handling    | try/except on all numeric inputs; boundary checks enforced  |
| Resource Efficiency | No external libraries; minimal memory footprint           |

---

## Author

**Parth**
B.Tech Computer Science Engineering
VIT Bhopal University | Reg. No: 26BCE10454
