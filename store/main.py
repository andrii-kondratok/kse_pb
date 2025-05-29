import add_product as add
from data import inventory
from data import transactions
import buy_product as buy
import utils
i = 1
while True:
    print("Меню дій: 1 — додати товар\n 2 — купити товар\n 3 — переглянути облік\n 0 — вийти")
    n = int(input(""))
    if n == 0:
        break
    elif n == 1:
        nama = input("Введіть назву товару")
        if nama not in inventory:
            add.add_product(inventory, nama, int(input("Введіть ціну товару")), int(input("Введіть кількість товару")))
        else:
            add.add_product(inventory, nama, inventory[nama]["price"], int(input("Введіть кількість товару")))
    elif n == 2:
        buy.buy_product(inventory, transactions, input("Введіть назву товару"), int(input("Введіть кількість товару")), i)
        i+=1
    elif n == 3:
        print(transactions)
    print(inventory)