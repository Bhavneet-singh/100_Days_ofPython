#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

choosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Your guess : ").lower()



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in range(len(choosen_word)):
  if choosen_word[i] == guess:
    print(True)
  else:
    print(False)
