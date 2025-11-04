# Exercise on lists operations & "If statement" & Join and slicing

import random,os, time

# Functions for game utilities
def sleep(second):
    time.sleep(second)

# clears the terminal screen
def clear_terminal():
    os.system('clear' if os.name == 'poix' else 'cls')

# Generate random word for the game
def genereat_word():
    random_word = random.choice(['world', 'life', 'beauty', 'love', 'play', 'meeting', 'loyalty', 'learning'])

    return list(random_word)

# Hangman pictures for each wrong guess
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
  |
=========''']

# Show game rules to player
def display_rules():
    "DISPLAIGN THE RULES OF GAME"
    print("""
            1. There is an execution platform wiht incomplete doll
            2. There is a word you have to guess
            3. Sevral dashes will appear equal the number's letter of word
            4. You enter your guess letter 
            5. If guessed letter good, than become the entered lettr in pleace of dash
            6. If your guess worng, life missing an attempt than a part of doll will be completed
            7. If you guessed all of letters good, than you win
            8. If the chances are over, than you losed
          
         ********** LETS GO! YOU HAVE FROM NOW 6 ATTEMPTS ***********""")
    
    input('\nIf you ready press enter to start...... \n')

clear_terminal()

# hold the readable word (string)
word_to_guess = ""

secret_word = genereat_word()

# Append the guess word to keep it like orginal
for character in secret_word:
    word_to_guess += character

# create a list of underscores matching the length of the secret word for display
dashes = ['_'] * len(secret_word)

# Track guessed letters
guessed_list = []

 # Player lives
life = 6

 # Game state
game_on = True

# Main game loop
while game_on:

    # show current hangman stage
    print(f'\n\n\nHang man game: \n',HANGMANPICS[6-life])

    # show the secret word as dashes
    print('\nSecret word:\n',' '.join(dashes),'\n')

    # remind the player they can ask for help/rules
    print(f'\n***Would you like to see rules? Type [ HELP ] ***\n\n')

    # Get player guess
    guessed = input('\nEnter gussing:  ').lower()

    # validate input contains only alphabetic characters
    if not guessed.isalpha():
        
        print(f"\nInvalid entry: [{guessed}]  ***\nEntry only most a character!\n")
        sleep(2)
    # validate that either a single character or the word 'help' was entered
    elif len(guessed) != 1 and  guessed != 'help':
        
        print(
            f"\nEntry [{guessed}] is unexpected ***\n*** Type only one character! ***\n** Or type [ HELP ] to see Rules! **\n")
        sleep(2)

    else:
        
        # validate if player wants to see rules 
        if guessed == 'help':

            display_rules()
            
        # Check if the guess in secret word or in guessed_list
        elif guessed not in secret_word and guessed not in guessed_list:

            print(f"\nWorng Gussed! ***\n")

            # decrement life because the guess was incorrect
            life -= 1

            # show remaining attempts if any left, else show final message
            if life != 0:
              print(f"\nYou have [{life}] attempts ***\n")

            else:
                print(f'******[ Your attempts are over! ]******')

            sleep(3)

        # check if letter is already guessed
        elif guessed not in secret_word and guessed in guessed_list:
            print(f"\nCharacter [{guessed}] is already guessed!\n")
            sleep(2)
            
        else:
            # correct guess branch: either a new correct guess or the letter appears in secret_word
            if guessed not in guessed_list and guessed in secret_word:

                # record the guessed character
                guessed_list.append(guessed)

                # reveal the guessed letter(s) in the dashes list
                for i in range(len(secret_word)):
                    
                    if guessed == secret_word[i]:
                        
                        secret_word[i] = dashes[i]
                        dashes[i] = guessed
            
                        break

                print('\nGood Guessed! ****\n\n')
                sleep(2)

    clear_terminal()        

    # if the player lost all lives, display final hangman, the original word and a losing message
    if life == 0:
        

        print("\n\n",HANGMANPICS[6 - life],'\n\n')

        print(f"\n\nSecret word: [ {word_to_guess.title()} ]\n\n")

        print("   ",'♨️'*11)
        print('\n***** YOU LOSE! *****\n')
        print("   ",'♨️'*11)

        game_on = False
    
    # if there are no underscores left in dashes, the player has guessed the whole word and wins
    if '_' not in dashes:
        
        print(f'\nGuessed Word: [ {word_to_guess.title()} ]\n\n')

        print(' 🥳🤑💯🤗♨️🤭♨️🤑💯🤑')
        print('\n***** YOU WIN! *****\n')
        print(' 🥳🤑💯🤗♨️🤭♨️🤑💯🤑')

        game_on = False
