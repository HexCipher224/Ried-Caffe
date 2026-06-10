def view_menu():
    print("\n===== CAFÉ MENU =====")

    menu_items = [
        {"name": "Coffee", "price": 150},
        {"name": "Tea", "price": 100},
        {"name": "Burger", "price": 350},
        {"name": "Cake", "price": 200},
    ]

    for item in menu_items:
        print(f"{item['name']} - KES {item['price']}")


def place_order():
    print("\n===== PLACE ORDER =====")

    customer_name = input("Enter customer name: ")
    item_name = input("Enter item name: ")
    quantity = input("Enter quantity: ")

    print("\nOrder Summary")
    print(f"Customer: {customer_name}")
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")

    print("\n⚠ Order processing not yet connected.")


def view_inventory():
    print("\n===== INVENTORY =====")
    print("Inventory not yet connected.")


def exit_program():
    print("\nGoodbye!")
    exit()