import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low # this can be high bc low=high
        feedback=input(f'If {guess} too high (H) if too low (L), or correct (C)')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print('wow Computer guess it right')

computer_guess(100)