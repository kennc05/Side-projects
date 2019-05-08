#Set the word to be guessed here
word='jason'

#Create a list to add and store the correct letters in the list
correct_letters=[] #The correct letters will be stored here
guessed_letters=[] #The incorrect letters will be stored here

print('welcome to Hangman! You have 10 guesses to try')

wordlength=len(word) #Count how long the word is

#if wordlength = 0 then that means its a win as all of it is guessed

guesses_left=10 #Setting how many guesses left


print('The word to guess is '+str(wordlength)+ ' letters long')


#Create a loop until the guesses left is 0
while guesses_left>0:
    wordguessed=['_' * wordlength] 
    print(wordguessed) #Print out spaces by how long the word is
    userguess=input('Enter to guess a letter: ')

    for char in userguess: #For every character in the letter the user entered

        #Check win or lose eligibility 
        if wordlength==1:
            print('winner!!')
            print('Well done for guessing the word '+word)
            guesses_left=0
            break

        if guesses_left==0:
            print('loser!!')
            print('The word was '+word)
            break

        
        if userguess in word:#If the letter the user guessed is in the word
            print('Nice! You got a letter!')
            guessposition=word.find(userguess) #Get the position of the letter in word
            letterguessed=(word[guessposition]) #Fetch the letter from the word
            correct_letters.insert(guessposition, letterguessed) #Add it to the correct letters list
            print('Position of word guessed '+str(guessposition)) 
            correctword=''.join(map(str,correct_letters)) #Convert the correct letter list to a string
            wordlength=wordlength-1 #Subtract letters to guess by 1
            print('Letters left to guess '+str(wordlength))
            guesses_left=guesses_left-1 #subtract guesses left by 1
            print('You have '+str(guesses_left)+' guesses left')
            print('The word so far is '+correctword)
            print(correct_letters)
            break #end the loop once found

   
        
        else:
            print('You did not get the right letter')
            guessed_letters.insert(0 ,userguess) #Add the wrong letter to the guess letter list
            print('Wrong letters attempted')
            print(guessed_letters)
            guesses_left=guesses_left-1
            print('You have '+str(guesses_left)+' guesses left')
            break#break the loop or else it will do it x times (how long the word is)


