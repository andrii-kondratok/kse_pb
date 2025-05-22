import geometry as geo
import converter as conv
import taxes
import math
import random
from datetime import datetime
import datetime as dt
import matplotlib as mpb
import matplotlib.pyplot as plt
print(geo.area(4,6))
print(conv.uah_to_usd(1000, 39.5))
print(conv.usd_to_uah(1000, 39.5))
print(taxes.calculate_income_tax(15000)+taxes.calculate_vat(15000))
print(math.sqrt(121))
print(math.sin(math.pi/2))
print(math.floor(7.8))
print(math.ceil(7.8))
a = random.randint(1,20)
b = random.randint(1,20)
c=a+b
print(f"Перший кубик: {a}","\n", f"Другий кубик: {b}", "\n", f"Сума: {c}")
date = input("Введіть дату народження у форматі рррр-мм-дд: \n")
real_date = datetime.strptime(date, "%Y-%m-%d")
print(real_date)
today = dt.date.today()
print(f"Ви прожили вже ", (today - real_date.date()).days, " днів!")
balance = 10000
iter = 0
all_bal = []
all_iter = []
while True:
    if balance<100 or iter==1000:
        break
    bet = int(input("Введіть слот, на який ви ставите ваші 100 гривень: \n Щов вивести баланс, напишіть 0 \n"))
    if bet == 0:
        break
    if bet == random.randint(1,37):
        print("Перемога!!!!!! Ви виграли дуже багато грошей")
        balance += 100*36
    else: 
        print("нам дуже шкода( ви програли....")
        balance-=100
    print(f"Ваш теперішній баланс = {balance}")
    all_bal.append(balance)
    iter+=1
    all_iter.append(iter)
print(f"Ви залишили казино із балансом у {balance}")
plt.plot(all_iter, all_bal)
plt.xlabel("Номер ітерації")
plt.ylabel("Баланс гравця")
plt.title("Gambling saves lives")
plt.show()