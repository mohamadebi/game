import random

word_bank = ["mirza", "pes", "real", "manchester", "green", "ford", "jeep", "mars"]
word = random.choice(word_bank)
blank = len(word)
mistake = 0
correct_guess = []
wrong_guess = ""
char_user = "q"

while mistake < 6:
    for i in range(len(word)):
        if word[i] in correct_guess:
            print(word[i], end=" ")
        else:
            print("-", end=" ")

    char_user = input("\nPlease insert a letter or guess the word: ").lower()

    if len(char_user) == 1:
        if char_user in word:
            print("✔✔ Nice! Your letter correct 💪 ✔✔")
            correct_guess.append(char_user)
        else:
            print("❌ OH sheet! Your letter incorrect ❌")
            wrong_guess += char_user
            mistake += 1
    elif len(char_user) == len(word) and char_user == word:
        print("Congratulations! You guessed the word correctly 👏👏")
        break
    else:
        mistake += 1
        print("Incorrect guess. Try again.")

    if set(correct_guess) == set(word):
        print("Congratulations! You guessed the word correctly!")
        break

    if mistake == 6:
        print("Game Over ⛔⛔⛔")
