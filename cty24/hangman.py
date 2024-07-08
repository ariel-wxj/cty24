import random

def random_word():
    words = ["python", "hangman", "program", "kilometer", "skibidi", "mississippi"]
    return random.choice(words).upper()

def display_hangman(guesses):
    stages = [
        "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
        "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
        "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
        "  +---+\n  O   |\n /|   |\n      |\n     ===",
        "  +---+\n  O   |\n  |   |\n      |\n     ===",
        "  +---+\n  O   |\n      |\n      |\n     ===",
        "  +---+\n      |\n      |\n      |\n     ==="
        
        
       
       
       
    ]
    return stages[guesses]

def play_hangman():
    word = random_word()
    word_length = "_" * len(word)
    guessed = False
    guessed_letters = []
    guesses = 6

    print("welcome to hangman !")
    print(display_hangman(guesses))
    print(word_length)
    print("\n")

    while not guessed and guesses > 0:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and str(guess):
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                guesses -= 1
                guessed_letters.append(guess)
            else:
                print(f"yippee {guess} is right !")
                guessed_letters.append(guess)
                word_as_list = list(word_length)
                for i in range(len(word)):
                    if word[i] == guess:
                        word_as_list[i] = guess
                word_length = "".join(word_as_list)
                if "_" not in word_length:
                    guessed = True
        else:
            print("Invalid guess.")
        
        print(display_hangman(guesses))
        print(word_length)
        print("\n")
    
    if guessed:
        print("yippee you won!")
    else:
        print(f"you suck l bozo, the word was {word}. womp womp")

if __name__ == "__main__":
    play_hangman()
