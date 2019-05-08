#set the default maximum score to 5
score=5

#define the special characters because python does not have an inbuilt function for special characters
special = "@!@£$%^&*"


print('Welcome to the secure password checker!')
password=input('Input password to be checked: ')

print (password)
#check if the length of the password is less than 6
if len(password)<6:
    print('X Passwords should be longer than 6 characters to be secure')
    score=score-1
else:
    print("✓ Password is longer than 6 characters")

#check if the password contains a digit 
if not any(char.isdigit() for char in password):
    print('X Passwords should at least have a digit')
    score=score-1
else:
    print("✓ Password has a digit")

#check if the password has an upper character
if not any(char.isupper() for char in password):
    print('X Passwords should have at least one upper letter')
    score=score-1
else:
    print("✓ Password has has a upper letter")

#check if the password has a lower character
if not any(char.islower() for char in password):
    print('X Passwords should have at least one lower letter')
    score=score-1
else:
    print("✓ Password has a lower letter")

#check if the password has a special character
if not any(char in special for char in password):
    print('X Passwords should have at least one special character')
    score=score-1
else:
    print("✓ Password has a special character")

print("")
print("Results")

#different levels of security based on results 
if score==5:
    print ("✓ Password is super strong! Nice one!!")
if score>3:
    print('Your password is moderately strong')
else:
    print('You should consider a different password. This is vulnerable.')

print("You scored "+str(score)+" out of 5")


