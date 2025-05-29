from data import inventory
from data import transactions
def buy_product(inventory, transactions, name, quantity, seller_id):
    if name not in inventory:
        print("Такого товару не існує")
    else:
        inventory[name]["quantity"] -= quantity
        transactions[seller_id] = {"Товар": name, "Сума покупки": quantity*inventory[name]["price"], "Кількість куплених одиниць": quantity}
        print(inventory)
        print(transactions)
        def print_check(n = 1):
            return "Товар:", name, "Кількість куплених одиниць: ", quantity, "Сума покупки:", quantity*inventory[name]["price"]
        print(print_check())
        return inventory and transactions
#transactions = buy_product(inventory, transactions, "Зрада", 20, 1)
#print(inventory)
#print("\n")
#print(transactions)

