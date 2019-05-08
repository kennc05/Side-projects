#Using the word import to import the random function
import random
#shuffle is also part of random, which allows a word to be shuffled
from random import shuffle

#Set the original word so that the code can compare what it is later
originword='jason'

#Create a list so that the word can be shuffled, shuffle only works on lists
word=list('jason')

#Shuffle the actual word
random.shuffle(word)

#The new scrambled word
scrambled= ''.join(word)


#Output the new scrambled word to the user
print ('Can you guess this word ' + scrambled)

lives=5 #Defining how many lives are remaining
guess=0 #Defining how many guesses the user has had


while lives>0:
    print('You have {} lives left'.format(lives) ) #Outputting how many lives
    userguess=input('What is the word? ')
    guess=guess+1
    if userguess == originword:#Compare input to original word
        print ('Well done! You got it in {} guesses'.format(guess))
        exit() #Quit the program
    else:
        lives=lives-1 #Deducting a life
        guess=guess+1 #Adding a guess to no. of guesses
        print ('Try again, you have {} remaining'.format(lives))


print('You used up all of your lives, sorry!') #End of program where all lives used
        
