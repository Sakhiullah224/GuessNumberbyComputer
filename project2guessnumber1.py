# # using simple code
import random
# random_number=random.randint(1,10)
# guess=0
# while guess!= random_number:
#     guess=int(input('Guess a number bw 1 and 10'))
#     if guess< random_number:
#         print('Enter some higher number')
#     elif guess> random_number:
#         print('Enter some lower number')
#     else:
#         print('wow you guess it correct')
#         break
# using functions and methods
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

guess(10)