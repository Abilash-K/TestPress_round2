import random

def word_guessing():
    words = ['rainbow', 'computer','board',]

    word = random.choice(words)
    print("Guess the word")

    guesses = ''
    turns = 12

    while turns > 0:
        display_word = ''
        for char in word:
            if char in guesses:
                display_word += char
            else:
                display_word += '_'

        print(display_word)

        if display_word == word:
            print("You Win! The word is:", word)
            break

        guess = input("Guess a character: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong guess!")
            print("You have", turns, 'guesses left')

            if turns == 0:
                print("You Loose. The word was:", word)
                break

word_guessing()
