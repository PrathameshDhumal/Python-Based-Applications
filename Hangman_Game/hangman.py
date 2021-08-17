
##############################################################
#
#Author:Prathamesh Dhumal
#Date:20/7/21
#About:Creating Hangman Game using Python
#
#############################################################
# import the random python module
import random
from hangman_guessing import guess_list

guessing_word = random.choice(guess_list).lower()
word_letters = len(guessing_word)

game_over = False
tries = 6

#Import the game name from hangman_life.py and print it at the game start:
from hangman_life import game_name
print(game_name)


print(f'The word you guessed is {guessing_word}')


result = []
for _ in range(word_letters):
    result += "_"

while not game_over:
    user_guessing = input("Guess a letter: ")

    if user_guessing in result:
        print(f"The letter you guess {user_guessing}")


    for position in range(word_letters):
        letter = guessing_word[position]
  
        if letter == user_guessing:
            result[position] = letter

    if user_guessing not in guessing_word:
   
        print(f"You guessed {user_guessing}, this letter is not in the word, You lose a try.")
      
        tries -= 1
        if tries == 0:
            game_over = True
            print("You are a loser, Game Over.")

    #Join all the elements in the result list and turn it into a String.
    print(f"{' '.join(result)}")

    #Check if the players has got all the right letters so they will win the game.
    if "_" not in result:
        game_over = True
        print("You are a winner, Congratulations.")

    # Import the lives from hangman_life.py module and make this error go away.
    from hangman_life import lives
    print(lives[tries])