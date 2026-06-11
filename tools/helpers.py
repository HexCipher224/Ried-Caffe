def format_currency(amount):
    """
    Formats numbers into currency style.
    """

    return f"Ksh {amount:.2f}"


def generate_receipt(customer, items, total):

    #Creates a simple receipt.


    receipt = "\n------ CAFE RECEIPT ------\n"

    receipt += f"Customer: {customer}\n"

    receipt += "\nItems:\n"

    for item in items:
        receipt += f"- {item}\n"

    receipt += f"\nTotal: {format_currency(total)}"

    receipt += "\n--------------------------"

    return receipt


def calculate_change(payment, total):

    #Calculates customer balance.
    

    return payment - total