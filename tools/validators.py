def validate_name(name):
    #check if item name is valid
    if not name:
        return False

    if name.strip() == "":
        return False

    return True

def validate_quantity(quantity):
    #checks is quantity is a positive integer
    try:
        quantity = int(quantity)
        if quantity > 0:
            return True

        return False

def validate_price(price):
    #checks if price is a postive number
    try:
        price = float(price)
        if price >= 0:
            return True

        return False

def validate_payment(amount, total):
    #checks if customer payment covers the bill.
    try:
        amount = float(amount)
        total = float(total)

        return amount >= total

    except ValueError:
        return False