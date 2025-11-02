# Exercise on lists operations & "If statement" & Join and slicing

import random,os, time


def sleep(second):
    time.sleep(second)


def clear_terminal():
    os.system('clear' if os.name == 'poix' else 'cls')


def genereat_word():
    random_word = random.choice(['world', 'life', 'beauty', 'love', 'play', 'meeting', 'loyalty', 'learning'])

    return list(random_word)


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

word_to_guess = ""

secret_word = genereat_word()
print(secret_word)

for character in secret_word:
    word_to_guess += character

dashes = ['_'] * len(secret_word)

guessed_list = []

life = 6

game_on = True

while game_on:
    print(secret_word)
    print(f'\n\n\nHang man game: \n',HANGMANPICS[6-life])

    print('\nSecret word:\n',' '.join(dashes),'\n')

    print(f'\n***Would you like to see rules? Type [ HELP ] ***\n\n')

    guessed = input('\nEnter gussing:  ').lower()

    if not guessed.isalpha():
        
        print(f"\nInvalid entry: [{guessed}]  ***\nEntry only most a character!\n")
        sleep(2)

    elif len(guessed) != 1 and  guessed != 'help':
        
        print(
            f"\nEntry [{guessed}] is unexpected ***\n*** Type only one character! ***\n** Or type [ HELP ] to see Rules! **\n")
        sleep(2)

    else:
        
        if guessed == 'help':
            display_rules()
            

        elif guessed not in secret_word and guessed not in guessed_list:
            print(f"\nWorng Gussed! ***\n")
            life -= 1

            if life != 0:
              print(f"\nYou have [{life}] attempts ***\n")

            else:
                print(f'******[ Your attempts are over! ]******')

            sleep(3)

        elif guessed not in secret_word and guessed in guessed_list:
            print(f"\nCharacter [{guessed}] is already guessed!\n")
            sleep(2)
            
        else:
             
            if guessed not in guessed_list or guessed in secret_word:

                guessed_list.append(guessed)

                for i in range(len(secret_word)):
                    
                    if guessed == secret_word[i]:
                        
                        secret_word[i] = dashes[i]
                        dashes[i] = guessed
            
                        break

                print('\nGood Guessed! ****\n\n')
                sleep(2)

    clear_terminal()        



    if life == 0:
        

        print("\n\n",HANGMANPICS[6 - life],'\n\n')

        print(f"\n\nSecret word: [ {word_to_guess.title()} ]\n\n")

        print("   ",'♨️'*11)
        print('\n***** YOU LOSE! *****\n')
        print("   ",'♨️'*11)

        game_on = False
    
    if '_' not in dashes:
        
        print(f'\nGuessed Word: [ {word_to_guess.title()} ]\n\n')

        print(' 🥳🤑💯🤗♨️🤭♨️🤑💯🤑')
        print('\n***** YOU WIN! *****\n')
        print(' 🥳🤑💯🤗♨️🤭♨️🤑💯🤑')

        game_on = False
