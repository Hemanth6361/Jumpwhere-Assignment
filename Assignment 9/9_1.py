import random

def generate_random_number():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def count_cows_and_bulls(secret_number, user_guess):
    cows, bulls = 0, 0
    for i in range(len(secret_number)):
        if secret_number[i] == user_guess[i]:
            cows += 1
        elif user_guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = input("Enter a 4-digit number with non-repeating digits: ")
        
        if not user_guess.isdigit() or len(user_guess) != 4 or len(set(user_guess)) != 4:
            print("Please enter a valid 4-digit number with non-repeating digits.")
            continue
        
        attempts += 1
        cows, bulls = count_cows_and_bulls(secret_number, user_guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    main()
