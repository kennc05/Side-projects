import random


characters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "@!@£$%^&*"
password = ""

#-------------------------------------------------

def passwordtest():

    score=5

    if len(password)<6:
        print('X Passwords should have more than 6 characters')
        score=score-1
    else:
        print("✓ Password is longer than 6 characters")
        
    if not any(char.isdigit() for char in password):
        print('X Passwords should contain at least one digit')
        score=score-1
    else:
        print("✓ Password has a digit")

    if not any(char.isupper() for char in password):
        print('X Passwords should have at least an upper letter')
        score=score-1
    else:
        print("✓ Password has has a capital letter")
        
    if not any(char.islower() for char in password):
        print('X Passwords should have at least an upper letter')
        score=score-1
    else:
        print("✓ Password has a lower letter")
        
    if not any(char in special for char in password):
        print('X A strong password would usually have a special charcter')
        score=score-1
    else:
        print("✓ Password has a special character")
        
    if score==5:
        print ("✓ Password is super strong! well done!!")

    print("You scored "+str(score)+" out of 5")



#------------------------------------------------
    
print ("Welcome to the random password generator!")

passwordlength=int(input("How long do you want your password to be?"))

specialchoice=input("Should there be special characters?")
upper=input("Should there be capital characters?")
number=input("Should there be number characters?")


while len(password)!=passwordlength:
    pwdchar=random.choice(characters)
    pwdupperchar=random.choice(characters)
    numberchar=random.choice(numbers)
    specialchar=random.choice(special)
    password=str(password)+str(pwdchar)
    if len(password)==passwordlength:
        break
    if specialchoice=="yes":
        password=str(password)+str(specialchar)
        if len(password)==passwordlength:
            break
    if upper=="yes":
        password=str(password)+str(pwdupperchar.upper())
        if len(password)==passwordlength:
            break
    if number=="yes":
        password=str(password)+str(numberchar)
        if len(password)==passwordlength:
            break

    
print ("Generated password: "+password)
print ("Testing password...")
passwordtest()

    
        
