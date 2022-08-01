import random
from words import words
import string

def get_valid_word(words):
    word=random.choice(words) # randomly chooses something from the word list
    while '-' in word or ' ' in word: # choose words with - or speace in them
        word=random.choice(words) # the loop iterate until we get the word that does not have - or space on it.
    return word.upper()

def hangman():
    word=get_valid_word(words)
    #print(word) # just to know in advance what is word to guess
    # keep track what already been guessed in the word
    word_letters=set(word)    #letters in the word
    #print (word_letters)  # to convert in a set
    alphabet=set(string.ascii_uppercase)  # set of all alphabets
    used_letters=set()  # define as a set of what the user has guessed already
    lives=6


    while len(word_letters) > 0 and lives >0:
        #letter used #' '.join(['a', 'b', 'cd'])-->'a b cd'
        print('you have' ,lives,' lives left , you have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('current word: ',' '.join(word_list))

        # getting user imput
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)# If this is the valid character in the alphabet that user has not use yet #then user going to add this to his or her used letter list
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # if the letter that user just guessed in the word, it would be removed from word_letters
                print(' ')
            else:
                lives=lives-1 # Take away a life if wrong
                print(user_letter,'letter is not in the word')

        elif user_letter in used_letters:
               print('you have already guesses that letter')

        else:
             print('That is not a valid letter, plz try again')
    # come to here when len(word_letters)==0 or when lives==0
    if lives == 0:
        print('you died , sorry, The word was ', word)
    else:
        print('wow, you guess the word ',word,)

hangman()  # call the function

