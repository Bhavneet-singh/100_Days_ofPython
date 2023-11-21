

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display =[]
for i in range(len(chosen_word)):
    display.append("_")
print(display)


while "_" in display:
    guess = input("Guess: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess


    print(display)


if "_" not in display:
    print("You Won")
else:
    print("You loose")
