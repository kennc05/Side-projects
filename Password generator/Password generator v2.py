#import the random library which allows you to randomly select anything
import random

#defining the character sets 
characters = "abcdefghijklmnopqrstuvwxyz"

#defining the number sets
numbers = "0123456789"

#defining the special characters
special = "@!@£$%^&*"

#creating the password variable which starts off as empty
password = ""


print ("Welcome to the random password generator!")

#let python select a number between 0 and 20
while True:
    try:
        passwordlength=int(input('Please input the length of your password which is multiple of 4: '))
        if passwordlength % 4 == 0:
            print('This is a multiple of 4!')
            break
        else:
            print('Please enter a multiple of 4 only!')
            
    except ValueError:
        print('That was not a number, please try again')
        passwordwordlength=int(input('Please input the length of your password which is a multiple of 4: '))

    
#create a loop that if the password length is not more than the random number,
#then  randomly select a lower case character, upper case character, number,
#special character and combine them into the password variable
while len(password)!=passwordlength:
    pwdchar=random.choice(characters)
    pwdupperchar=random.choice(characters)
    numberchar=random.choice(numbers)
    specialchar=random.choice(special)
    password=str(password)+str(pwdchar)+str(specialchar)+str(pwdupperchar.upper())+str(numberchar)


#print password and print the length
print ("Generated password: "+password)
print ("Password length is: "+str(len(password)))

    
