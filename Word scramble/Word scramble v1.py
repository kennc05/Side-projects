import random
from random import shuffle

originword='jason'
word=list('jason')
random.shuffle(word)
scrambled= ''.join(word)



print ('Can you guess this word ' + scrambled)

lives=5
guess = 0


while lives>0:
    print('You have {} lives left'.format(lives) )
    userguess=input('What is the word? ')
    guess=guess+1
    if userguess == originword:
        print ('Well done! You got it in {} guesses'.format(guess))
        exit()
    else:
        lives=lives-1
        print ('Try again, you have {} remaining'.format(lives))


print('You used up all of your lives, sorry!')
        
