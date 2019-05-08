import random


characters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "@!@£$%^&*"
password = ""


print ("Welcome to the random password generator!")

passwordlength=random.randint(0,20)


while len(password)<=passwordlength:
    pwdchar=random.choice(characters)
    pwdupperchar=random.choice(characters)
    numberchar=random.choice(numbers)
    specialchar=random.choice(special)
    password=str(password)+str(pwdchar)+str(specialchar)+str(pwdupperchar.upper())+str(numberchar)


print ("Generated password: "+password)
print ("Password length is: "+str(len(password)))

    
