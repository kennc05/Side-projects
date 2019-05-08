print('The grid layout')
print('0|1|2\n3|4|5\n6|7|8')
print(' ')

#defines a valid input list to be checked against when the user enters their choice
valid=['X','0']


#Creating a board from a list which allows a numbered grid to be made 
board = ['_'] * 9
def print_board():
  print(board[0] + '|' + board[1] + '|' + board[2])
  print(board[3] + '|' + board[4] + '|' + board[5])
  print(board[6] + '|' + board[7] + '|' + board[8])
  
print_board() #This runs the routine to print the board 

#asking for player 1 input

print('Welcome to tic tac toe!')


player1=input('player 1. Choose either X or 0')
player2=''

while player1!='X' or '0': #Keep asking for user input until a valid entry
  if player1=='0':
    player2='X'
    print('player 2 you are X')
    break

  if player1=='X':
    player2='0'
    print('player 2 you are 0')
    break

  else:
    print('That was not a valid input! Please try again')
    player1=input('player 1. Choose either X or 0')



winner=0 #variable to see if there is a winner or not 

def winner_check():

  global winner

  #These are all of the possible win combinaitons within the game

  if board[0] == 'X' and board[1]=='X' and board[2] == 'X':
     print('player X won!!')
     winner=winner+1
  
  elif board[0] == '0' and board[1]== '0' and board[2] == '0':
    print('player O won!!')
    winner=winner+1

  elif board[3] == 'X' and board[4]== 'X' and board[5] == 'X':
    print('player X won!!')
    winner=winner+1

  elif board[3] == '0' and board[4]== '0' and board[5] == '0':
    print('player 0 won!!')
    winner=winner+1
    
  elif board[6] == 'X' and board[7]== 'X' and board[8] == 'X':
    print('player X won!!')
    winner=winner+1

  elif board[6] == '0' and board[7]== '0' and board[8] == '0':
    print('player 0 won!!')
    winner=winner+1 

  elif board[0] == 'X' and board[3]== 'X' and board[6] == 'X':
    print('player X won!!')
    winner=winner+1 

  elif board[0] == '0' and board[3]== '0' and board[6] == '0':
    print('player 0 won!!')
    winner=winner+1 

  elif board[1] == 'X' and board[4]== 'X' and board[7] == 'X':
      print('player X won!!')
      winner=winner+1    

  elif board[1] == '0' and board[4]== '0' and board[7] == '0':
      print('player 0 won!!')
      winner=winner+1   

  elif board[2] == 'X' and board[5]== 'X' and board[8] == 'X':
      print('player X won!!')
      winner=winner+1       

  elif board[2] == '0' and board[5]== '0' and board[8] == '0':
      print('player 0 won!!')
      winner=winner+1   

  elif board[2] == 'X' and board[4]== 'X' and board[6] == 'X':
      print('player X won!!')
      winner=winner+1   

  elif board[2] == '0' and board[4]== '0' and board[6] == '0':
      print('player 0 won!!')
      winner=winner+1  

  elif board[0] == 'X' and board[4]== 'X' and board[8] == 'X':
      print('player X won!!')
      winner=winner+1  

  elif board[0] == '0' and board[4]== '0' and board[8] == '0':
      print('player 0 won!!')
      winner=winner+1

  #If it is a draw, the number of goes should equal to 8 with no winning matches and ends the game
  elif goes==9:
    print('It is a draw!')
    winner=winner+1
    
chosenpositions=[''] #Define a list that the game will add to when someone choses a number 

goes=0 #sets the number of goes to 0

while winner!=1:#A loop to ask for inputs while there hasn't been a winner

  while True: #True means to continue the loop until the code reaches the line 'break'
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError: #ValueError means if the input is not an integer
      print('That was not a number! Please try again')
      continue
    else:
      break #Ends there loop if there is a value input


  while int(x)>8: #If the user inputs a number which is more than 8
    print('Only below 8 please')
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError: #If the user tries to not enter a number
      print('That was not a number! Please try again')
      continue
    if int(x)>8: #If the input is still more than x
      continue #Continue the loop
    else:
      x=int(x)
      break #Define that x is an integer 


  while x in chosenpositions: #Checks if the user input is already in the chosenpositions list 
    print('that position has been taken! try again')
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError: #If the user tries to not enter a number
      print('That was not a number! Please try again')
      continue
    if x in chosenpositions:
      continue #If the input is still in chosen positions continue the loop 
    else:
      x=int(x) #Otherwise end the loop and set X as an integer and not a string 
      break
    
  else:
    x=int(x)
    print('You chose, position '+str(x)) #Print the position that they chose
    board[x] = player1 #The position chosen on the board will be changed to player 1's letter
    chosenpositions.insert(0,x) #Insert the position chosen into the chosen positions list
    print_board() #Print the board with the changes
    goes=goes+1 #Add 1 to the number of goes
    winner_check() #Run the routine to check if there is a winner
    if winner==1:
      break#If there is a winner, break the loop

  while True:
    try:
      y=int(input('Player 2 ('+str(player2)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    else:
      break


  while int(y)>8:
    print('Only below 8 please')
    try:
      y=int(input('Player 1 ('+str(player2)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    if int(y)>8:
      continue
    else:
      y=int(y)
      break


  while y in chosenpositions:
    print('that position has been taken! try again')
    try:
      y=int(input('Player 2 ('+str(player2)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    else:
      y=int(y)
      break
    
  else:
    y=int(y)
    print('You chose, position '+str(y))
    board[y] = player2
    chosenpositions.insert(0,y)
    print_board()
    goes=goes+1
    winner_check()
    if winner==1:
      break


