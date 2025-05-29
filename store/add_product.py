from data import inventory
import utils
def add_product(inventory, name, price, quantity):
    print(price)
    if utils.is_valid_price(price) is True:
        if name not in inventory:
            inventory[name] = {"price": price, "quantity": quantity}
            return inventory
        else:
            inventory[name]["quantity"] += quantity
            return inventory
    else:
        return "Вибачте, ціна не валідна"
inventory = add_product(inventory, "Зрада", 10, 20)
print(inventory)