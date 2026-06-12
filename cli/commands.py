from services import (
    InsufficientPaymentError,
    InvalidQuantityError,
    OrderService,
    OrderServiceError,
    PaymentService,
    ProductNotFoundError,
)


def view_menu():
    print("\n===== CAFÉ MENU =====")

    order_service = OrderService()

    for product in order_service.list_products():
        print(f"{product['productId']}. {product['name']} - KES {product['price']:.2f}")


def place_order():
    print("\n===== PLACE ORDER =====")

    customer_name = input("Enter customer name: ")
    item_identifier = input("Enter item ID or name: ")
    quantity = input("Enter quantity: ")

    try:
        product_identifier = int(item_identifier)
    except ValueError:
        product_identifier = item_identifier

    order_service = OrderService()
    payment_service = PaymentService()

    try:
        order = order_service.create_order(customer_name, product_identifier, quantity)
    except (OrderServiceError, InvalidQuantityError, ProductNotFoundError) as error:
        print(f"\n❌ {error}")
        return

    print("\nOrder Summary")
    print(order.summary())

    payment_method = input("Enter payment method [cash]: ").strip() or "cash"

    try:
        amount_paid = float(input(f"Enter amount paid (KES {order.total:.2f}): "))
        payment_result = payment_service.process_payment(order, amount_paid, payment_method)
    except ValueError:
        print("\n❌ Payment amount must be a number.")
        return
    except InsufficientPaymentError as error:
        print(f"\n❌ {error}")
        return

    print("\n" + payment_service.format_payment_summary(order, payment_result))
    print("\n" + order_service.render_receipt(order))


def view_inventory():
    print("\n===== INVENTORY =====")
    order_service = OrderService()

    for product in order_service.list_products():
        print(f"{product['productId']}. {product['name']} - Stock: {product['stock']}")


def exit_program():
    print("\nGoodbye!")
    exit()