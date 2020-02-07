# Hangman game
# NOTE: I already made a hangman game over the summer (I showed you this) so I edited it to fit with this assignment
# I can show it to you again if you'd like
import random
# PSEUDOCODE
# setup your game by doing the following
mylistofwords = ["discombobulated", "sophistication", "emboss", "canoodle", "skedaddle", "gobbledygook", "materialize",
                 "imperatively", "myriad", "sentimentality", "physiological", "cliche", "fisticuffs", "dimwit"]
chosen = random.choice(mylistofwords)
wordlength = len(chosen)
done = False
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]
# in a loop, do the following:
# display the hangman using the gallows *
# display the used letters so the user knows what has been selected *
# display the length of the word to the user using blank spaces and used letters *
# prompt the user to guess a letter *
# don't allow the user to select the same letter twice *
# if the guess is incorrect increment incorrect_guesses by 1 *
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program *
# if the user gets all the correct letters, tell the user they won *
# ask if they want to play again *


def get_current_word(choice, guessed):  # obtains the current word for the user to guess
    word = ""

    for letter in choice:
        if letter in guessed:
            word += letter
        else:
            word += " _ "
    return word


def play_again_func():  # function to play again
    answer = input("Would you like to play again? (yes or no) ")
    if answer.lower() == "yes":
        return answer


while not done:  # game loop
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        incorrect_guesses = 0
        gallow_number = 0
        print("Your word is", wordlength, "letters long.")
        guessedletters = []

        while incorrect_guesses < 6:  # in the directions you wrote 8, but there were 6 graphics
            print("\nThe letters you have used: ", guessedletters)
            print(gallows[gallow_number])
            player_guess = input("\nGuess a letter of the alphabet: ").lower()

            if player_guess not in alphabet:
                print("That is not a letter of the alphabet.\n")

            elif player_guess in guessedletters:
                print("You have already guessed that letter.\n")

            elif player_guess not in chosen:  # if user chooses incorrect letter
                print("\nThat is incorrect!")
                incorrect_guesses += 1
                guessedletters.append(player_guess)
                word = get_current_word(chosen, guessedletters)
                print(word)
                gallow_number += 1

            else:  # if user guesses correctly
                guessedletters.append(player_guess)
                if player_guess in chosen:
                    print("You guessed correctly!\n")
                    word = get_current_word(chosen, guessedletters)
                    print(word)

                    if ' _ ' not in word:
                        print("\nYou won!")
                        done = True
                        del mylistofwords[mylistofwords.index(chosen)]
                        break

        if incorrect_guesses == 6:  # if the user has lost
            print(gallows[6])
            print("You have taken too many guesses to guess your word; you lose! The word was", chosen)
            done = True

        if mylistofwords == []:  # if the user has guessed all of the words in the list (by playing again)
            print("You have used up all the words!")
            break

        if done:  # if the user has finished the game
            if play_again_func():  # if the user wants to play again
                done = False
                guessedletters = []
                chosen = random.choice(mylistofwords)
                wordlength = len(chosen)


