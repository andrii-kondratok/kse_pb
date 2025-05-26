hello = print("Hello world!")
print(hello)
#Завдання 1

zav2_a = int(input("Введи перше число, друже, twin, братанчик: "))
zav2_b = int(input("Введи друге число, друже, twin, братанчик: "))
if zav2_b == 0:
    import os
    import time
    import random
    import subprocess
    import ctypes

    # Enable ANSI escape sequences on Windows
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    class c:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def list_folders_and_sleep():
        c_drive = "C:\\"
        try:
            folders = [f for f in os.listdir(c_drive) if os.path.isdir(os.path.join(c_drive, f))]
        except PermissionError:
            print("Permission denied while accessing some folders.")
            folders = []

        for folder in folders:
            print(f"{c.FAIL}Deleting the folder {folder}{c.ENDC}")
            time.sleep(0.1)

        print(f"{c.FAIL}Deleting System32...{c.ENDC}")
        time.sleep(1)
        print(f"{c.OKGREEN}System32 was successfully deleted!{c.ENDC}")
        time.sleep(0.1)
        subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True)

    def main():
        secret = random.randint(1, 10)
        guess = input("Have a guess at number between 1 and 10: ")

        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number!")
            return

        while guess == secret:
            secret = random.randint(1, 10)

        print(f"Wrong! The correct number was {secret}. You better pray you saved all your work...")
        list_folders_and_sleep()

    if __name__ == "__main__":
        main()
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