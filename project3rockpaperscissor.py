#make a program to see who choses the heavier object from rock,paper and scissor
# condition is r>s,s>p,p>r
import random
def play():
    computer=random.choice(['r','p','s'])
    print(computer) # just to know what compluter has choiced
    user= input ("what is your choice, 'r' for rock,'p' for paper  or 's' for scissor")

    if user==computer:
        return 'its a tie'
    elif is_win(user,computer):
        return 'you won'
    else:
        return 'you lost'



def is_win(player,opponent):
    # return true if player win
    # condition r>s,s>p,p>r
    if (player=='r' and opponent=='s' or player=='s' and opponent=='p' or player=='p' and opponent=='r'):
        return True
print(play())