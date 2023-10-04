import random

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman(word):
    print("Welcome to Hangman!")
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess your letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect!")
            print(f"You have {attempts} {'chance' if attempts == 1 else 'chances'} left to guess.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was: {word}")

def main():
    words = read_words_from_file("words.txt")
    while True:
        word_to_guess = choose_random_word(words)
        play_hangman(word_to_guess)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
