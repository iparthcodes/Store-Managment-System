# main.py
# Store Management System - Main Entry Point
# Run: python main.py

from inventory import view_products, add_product, update_product, delete_product, search_product
from billing   import create_bill, view_bills
from reports   import sales_summary, low_stock_alert, top_selling


def main():
    print("=" * 42)
    print("     STORE MANAGEMENT SYSTEM")
    print("     Python Essentials Project")
    print("=" * 42)

    while True:
        print("\n---------- MAIN MENU ----------")
        print(" 1. View All Products")
        print(" 2. Add Product")
        print(" 3. Update Product")
        print(" 4. Delete Product")
        print(" 5. Search Product")
        print(" 6. Create Bill")
        print(" 7. View Recent Bills")
        print(" 8. Sales Summary")
        print(" 9. Low Stock Alert")
        print("10. Top Selling Products")
        print(" 0. Exit")
        print("-------------------------------")

        choice = input("Enter choice: ").strip()

        if   choice == "1":  view_products()
        elif choice == "2":  add_product()
        elif choice == "3":  update_product()
        elif choice == "4":  delete_product()
        elif choice == "5":  search_product()
        elif choice == "6":  create_bill()
        elif choice == "7":  view_bills()
        elif choice == "8":  sales_summary()
        elif choice == "9":  low_stock_alert()
        elif choice == "10": top_selling()
        elif choice == "0":
            print("\nThank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
