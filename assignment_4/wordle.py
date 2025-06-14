import random

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
secret_word = random.choice(words)

tries = 1
word_len = len(secret_word)

print("Welcome to Wordle!")
print("Guess the 5-letter word. You have 6 tries.")

while tries<=6:
    guess = input(f"Attempt {tries}/6 – Enter guess: ").lower()
    
    if len(guess)!=word_len:
        print("Wrong length. Expected", word_len)
        continue

    if guess==secret_word:
        print("You win!!!")
        break

    result=[]
    for i in range(word_len):
        ch = guess[i]
        if ch==secret_word[i]:
            result.append('correct')
        elif ch in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i+=1

    display=[]
    j=0
    while j<word_len:
        s = guess[j]
        res = result[j]
        if res=='correct':
            display.append("["+s.upper()+"]")
        elif res=='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1

    junk = ''.join([c for c in display if c])
    print("Result:", ' '.join(display))
    tries += 1
else:
    final = secret_word
    print("You lose! The word was:", final)