import random
from logo import logo

print(logo)
print("Welcome to the Number_guessing Game ")

def hard(GUESS):
    lives = 6 
    while lives > 0:
        guess = int(input("Guess the number?: "))

        if guess < GUESS:
            print("Too Low")
            print(f'The number of lives remaining {lives}')
            lives -=1

        elif guess > GUESS:
            print('Too High')
            print(f'The number of lives remaining {lives}')
            lives -= 1
        else:
            return "You guessed right"
    return f'Out of lives correct number was {GUESS}'


def easy(GUESS):
    lives = 10
    while lives > 0:

        guess = int(input("Guess the number?: ")) 
        if guess < GUESS:
            print("Too Low")
            print(f'The number of lives remaining {lives}')
            lives -=1

        elif guess > GUESS:
            print('Too High')
            print(f'The number of lives remaining {lives}')
            lives -= 1
        else:
            return "You guessed right"
    return f'Out of lives correct number was {GUESS}'

GUESS = random.randint(1, 100)
mode = input("Choose a difficulty easy or hard? : ")


if mode == 'hard':
    output =hard(GUESS)
    print(output)

elif mode == 'easy':
    output =easy( GUESS)
    print(output)




