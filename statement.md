# Project Statement

## Problem Statement

Small retail shops typically manage inventory and billing using handwritten registers, which leads to stock miscounts, slow billing, and no visibility into sales trends. This project provides a simple Python-based terminal system to handle these operations digitally — without needing any internet connection, external tools, or database.

---

## Scope

The system covers three core areas:

1. **Inventory Management** – add, view, update, delete, and search products
2. **Billing** – generate itemised bills with automatic tax calculation and stock deduction
3. **Reports** – view revenue totals, low stock alerts, and top selling products

Data is stored in Python dictionaries and lists via a shared `storage.py` module that rewrites itself after every change, so all data persists even after the program exits. No external libraries or database are used.

---

## Target Users

Small shop owners, canteen managers, kiosk operators, or anyone who needs a simple digital system to replace paper-based stock and billing records.

---

## High-Level Features

| Feature               | Description                                          |
|-----------------------|------------------------------------------------------|
| View Products         | Display all products with low stock warnings         |
| Add / Update / Delete | Manage product catalogue with validation             |
| Search Product        | Find products by name keyword                        |
| Create Bill           | Generate receipt with 5% GST and deduct stock        |
| View Recent Bills     | Show last 5 transactions                             |
| Sales Summary         | Total bills, revenue, and tax collected              |
| Low Stock Alert       | Flag items with 5 or fewer units remaining           |
| Top Selling Products  | Rank products by units sold                          |
| Unit Tests            | 17 automated tests covering all core logic           |

---

## Functional Requirements

1. The system shall allow the user to view all products with their ID, name, price, and stock quantity, with a low stock warning for items at or below 5 units.
2. The system shall allow adding a new product with a unique ID, name, price, and quantity, with validation on all fields.
3. The system shall allow updating the price and stock quantity of any existing product.
4. The system shall allow deleting a product after a confirmation prompt.
5. The system shall allow searching for products by name using a partial, case-insensitive keyword.
6. The system shall generate an itemised bill with 5% GST, automatically deduct sold quantities from stock, and save the sale record.
7. The system shall display the last 5 bills with customer name, item count, and total amount.
8. The system shall show a sales summary with total number of bills, total revenue, and total tax collected.
9. The system shall alert the user to all products with 5 or fewer units remaining.
10. The system shall rank all sold products by total units sold across all bills.

---

## Non-Functional Requirements

1. **Performance** – All lookups use Python dicts (O(1)); no database queries or heavy I/O overhead.
2. **Usability** – Numbered menu, inline prompts, and clear success/error messages for every action.
3. **Reliability** – All user inputs are validated; invalid entries print errors and re-prompt rather than crashing.
4. **Maintainability** – Code split into 6 focused modules with a single shared `save.py` and `storage.py` data layer.
5. **Error Handling** – `try/except ValueError` wraps every numeric input; boundary checks prevent negative values, zero quantities, and overselling.
6. **Resource Efficiency** – Standard library only; no pip installs required; runs on any Python 3.6+ environment.
