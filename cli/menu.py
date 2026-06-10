from cli.commands import (
    view_menu,
    place_order,
    view_inventory,
    exit_program
)


def start_menu():
    while True:
        print("\n" + "=" * 40)
        print("      WELCOME TO PYTHON CAFÉ")
        print("=" * 40)

        print("1. View Menu")
        print("2. Place Order")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()

        elif choice == "2":
            place_order()

        elif choice == "3":
            view_inventory()

        elif choice == "4":
            exit_program()

        else:
            print("❌ Invalid option. Please try again.")