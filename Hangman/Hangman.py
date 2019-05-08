word='jason'


correct_letters=[] 
guessed_letters=[]

print('welcome to Hangman! You have 10 guesses to try')

wordlength=len(word) 



guesses_left=10 


print('The word to guess is '+str(wordlength)+' letters long')



while guesses_left>0:
    wordguessed=['_' * wordlength] 
    print(wordguessed) 
    userguess=input('Enter to guess a letter: ')

    for char in userguess: 

    
        if wordlength==1:
            print('winner!!')
            print('Well done for guessing the word '+word)
            guesses_left=0
            break

        if guesses_left==0:
            print('loser!!')
            print('The word was '+word)
            break

        
        if userguess in word:
            print('Nice! You got a letter!')
            guessposition=word.find(userguess) 
            letterguessed=(word[guessposition]) 
            correct_letters.insert(guessposition, letterguessed) 
            print('Position of word guessed '+str(guessposition)) 
            correctword=''.join(map(str,correct_letters)) 
            wordlength=wordlength-1 
            print('Letters left to guess '+str(wordlength))
            guesses_left=guesses_left-1 
            print('You have '+str(guesses_left)+' guesses left')
            print('The word so far is '+correctword)
            print(correct_letters)
            break 

   
        
        else:
            print('You did not get the right letter')
            guessed_letters.insert(0 ,userguess) #Add the wrong letter to the guess letter list
            print('Wrong letters attempted')
            print(guessed_letters)
            guesses_left=guesses_left-1
            print('You have '+str(guesses_left)+' guesses left')
            break#break the loop or else it will do it x times (how long the word is)


