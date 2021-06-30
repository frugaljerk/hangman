import random
from words import words, man
import string

def validate_word(words):
    word = random.choice(words) #randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    #Keep track on user inputs
    word = validate_word(words)

    letters_word = set(word) #letters in the word
    letters_used = set() #user's guesses
    alphabets = set(string.ascii_uppercase)
    lives = 10
    #adding user input to the sets
    while len(letters_word) > 0 and lives > 0 :
        #letter used
        # ' '.join(['a', 'b','cd']) ---> a b cd
        print(f'You have {lives} remaing and you have used these letters:' + ' '.join(letters_used))

        #what current word is (ie W-RD)
        word_list = [letters if letters in letters_used else '-' for letters in word ]
        print("Current word: ", ' '.join(word_list))
        print(man[10-lives])

        user_input = input("Please enter a letter:").upper()
        if user_input in alphabets - letters_used:
            letters_used.add(user_input)
            if user_input in letters_word:
                letters_word.remove(user_input)
            else:
                lives = lives - 1 #minus one life for incorrect guess
                print('Letter is not in the word')

        elif user_input in letters_used:
            print('You have used this letter. Please try again:')
        else:
            print('Invalid character. Please try again:')

    if lives == 0:
        print(man[10])
        print(f'Sorry you died. The word was {word}')
    else:
        print(man[10-lives])
        print(f'You WON!! The word wsa {word}')



hangman()