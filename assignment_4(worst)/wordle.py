import functions
#Це файлик для запуску гри, гиги
while True:
    functions.play_game()
    play_again = input("One more round? \n").lower()
    if play_again != "yes":
        print("Ну як хочеш, It's not like I'm sad or anything. *blushes and cries in anime maner, cuz I'm lowkey tsundere*")
        break