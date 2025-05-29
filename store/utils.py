def is_valid_price(value):
    if value<=0:
        return False
    else:
        return True
def is_valid_quantity(value):
    if value<=0:
        return False
    else:
        return True
def format_currency(amount):
    return str(round(amount, 2)) + " грн"