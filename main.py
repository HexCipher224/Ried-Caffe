""" from cli.menu import start_menu

if __name__ == "__main__":
    start_menu() """

import sys

from cli.menu import start_menu
from services.payment_service import (
    PaymentService,
    PaymentResult,
    PaymentError) 

from cafe.function import (
    list_products,
    create_product,
    update_stock
)

if __name__ == "__main__":

    # No command supplied → open menu
    if len(sys.argv) == 1:
        start_menu()

    # Commands
    elif sys.argv[1] == "list-products":
        list_products()

    elif sys.argv[1] == "add-product":
        create_product()

    elif sys.argv[1] == "update-stock":
        update_stock()

    elif sys.argv[1] == " PaymentService":
        PaymentService()

    elif sys.argv[1] == "PaymentResult":
        PaymentResult()

    elif sys.argv[1] == "PaymentError":
        PaymentError()

    else:
        print("Unknown command")