from cli.commands import (
    view_menu,
    place_order,
    payment_service,
    exit_program
)


def start_menu():
    while True:
        print("\n" + "=" * 40)
        print("      WELCOME TO PYTHON CAFÉ")
        print("=" * 40)

        print("1. View Menu")
        print("2. Place Order")
        print("3. Payment service")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()

        elif choice == "2":
            place_order()

        elif choice == "3":
            payment_service()

        elif choice == "4":
            exit_program()

        else:
            print("❌ Invalid option. Please try again.")