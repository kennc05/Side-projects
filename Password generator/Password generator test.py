import random


characters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "@!@£$%^&*"
password = ""


print ("Welcome to the random password generator!")

passwordlength=24
##random.randint(5,20)


while len(password)!=passwordlength:
    pwdchar=random.choice(characters)
    pwdupperchar=random.choice(characters)
    numberchar=random.choice(numbers)
    specialchar=random.choice(special)
    try:
        password=str(password)+str(pwdchar)
        password=str(password)+str(specialchar)
        password=str(password)+str(pwdupperchar.upper())
        password=str(password)+str(numberchar)
    except:
        break

    
print ("Generated password: "+password)
print ("Password length is: "+str(len(password)))

    
        
####might have to individually add each part because it cant take odd numbers
