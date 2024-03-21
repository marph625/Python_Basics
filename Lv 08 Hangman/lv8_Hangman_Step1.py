import random

#   _  _                                
#  | || |__ _ _ _  __ _ _ __  __ _ _ _  
#  | __ / _` | ' \/ _` | '  \/ _` | ' \ 
#  |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
#                 |___/                 

# Step 1

word_list = ["Dragonball", "JavaScript", "Python", "Programmieren", "Supercalifragilisticexpialigetisch"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

"""counter = 1

while counter != 6:
    chosen_word = random.choice(word_list)
    print(counter, "=>", chosen_word)
    counter += 1
"""
# make chosen_word lowercase to avoid issues when checking

print("Beepboop! Calculating...choosing word...finished!")
chosen_word = random.choice(word_list).lower()

# make a string with as many blanks as letters in guess
# Underscore times the length of the given string

blank_word = "_ " * len(chosen_word)
print(blank_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter\n")
guess = guess.lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

""" if guess in chosen_word:
    print(guess, "is in", chosen_word)
else:
    print("Try again") """
