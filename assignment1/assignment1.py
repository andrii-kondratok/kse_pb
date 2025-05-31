hello = print("Hello world!")
#Завдання 1

zav2_a = int(input("Введи перше число, друже, twin, братанчик: "))
zav2_b = int(input("Введи друге число, друже, twin, братанчик: "))
if zav2_b == 0:
    print("Не можна ділити на нуль, дуринда ")
else: print(zav2_a + zav2_b, "\n", zav2_a - zav2_b, "\n", zav2_a * zav2_b, "\n", zav2_a / zav2_b)
#Завдання 2

str_1 = "Едік"
str_2 = "Коваленко"
str_f = str_1 + " " + str_2
print(str_f)
print(len(str_f))
#Завдання 3

zav4 = int(input("Ayo, twin, введи число, twin 🥀"))
if zav4%2==0:
    print("Even")
else:
    print("Odd")
#Завдання 4

for i in range (1,11):
    print(i)
#Завдання 5

zav6 = int(input("Ayo, twin, введи число, twin 🥀"))
if zav6>0:
    print("Positive")
elif zav6==0:
    print("Zero")
else:
    print("Niggative")
#Завдання 6
for i in range(1,11):
    if i%2==0:
        print(i)
#Завдання 7

zav8 = int(input("Ayo, twin, введи число, twin 🥀"))
summa_bro = 0
for i in range(1, zav8+1):
    summa_bro += i
    print(summa_bro)
print(summa_bro,"\n")
#Завдання 8
lst9 = []
for i in range(1,11):
    lst9.append(i)
#print(lst9[::-1])
lst9.sort(reverse = True)
for i in lst9:
    print(i)
print("\n","\n","\n","\n")
#Завдання 9

for i in range(1,10):
    if i == 7:
        break
    elif i == 5:
        continue
    else: 
        print(i)