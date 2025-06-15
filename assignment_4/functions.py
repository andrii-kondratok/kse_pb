import random
def choose_word(list_of_words):
    secret_word = random.choice(list_of_words)
    return secret_word

def generate_result(guess, secret_word):
    result = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result


def display_result(guess, result):
    display = []
    for i, res in enumerate(result):
        if res == 'correct':
            display.append(f"[{guess[i].upper()}]")
        elif res == 'present':
            display.append(f"({guess[i]})")
        else:
            display.append(f" {guess[i]} ")
    return ''.join(display)


list_of_words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
def play_game():
    secret_word = choose_word(list_of_words)
    secret_word_len = len(secret_word)
    tries = 1

    print("""Welcome to Wordle!
    Guess the 5-letter word. You have 6 tries.""")

    while tries <= 6:
        guess = input(f"Attempt {tries}/6 – Enter guess: ").lower()
        if guess:
            print("Обробка відповіді....")
        else:
            print("Введи слово, це гра про слова")
            continue
        if not guess.isalpha():
            print("Хитрий лис у фарбу впав, як говорить моя мудрість.... Вводь тільки букви")
            continue
        
        if len(guess)!=secret_word_len:
            print(f"Wrong length. Expected {secret_word_len}")
            continue

        if guess==secret_word:
            print("You win!!!")
            break
        result = generate_result(guess, secret_word)
        print("Result:", display_result(guess, result))
        tries += 1
    else:
        print(f"You lose! The word was: {secret_word}")