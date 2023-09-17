import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("Enter 1 for rock, 2 for paper, 3 for scissors: ")
user_input = int(user_input)  # Convert user_input to an integer

# List of choices
choices = [rock, paper, scissors]

# Randomly select a choice for the computer
computer_response = random.choice(choices)

# Print the user and computer choices
print(f"Your choice:\n{choices[user_input - 1]}")
print(f"Computer's choice:\n{computer_response}")

# Comparing the choices
if user_input == 1:
    if computer_response == paper:
        print("You lose!")
    elif computer_response == rock:
        print("It's a tie!")
    else:
        print("You win!")
elif user_input == 2:
    if computer_response == scissors:
        print("You lose!")
    elif computer_response == paper:
        print("It's a tie!")
    else:
        print("You win!")
elif user_input == 3:
    if computer_response == rock:
        print("You lose!")
    elif computer_response == scissors:
        print("It's a tie!")
    else:
        print("You win!")
else:
    print("Invalid input. Please enter 1 for rock, 2 for paper, or 3 for scissors.")
