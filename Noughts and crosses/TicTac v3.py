print('The grid layout')
print('0|1|2\n3|4|5\n6|7|8')
print(' ')
valid=['X','0']

board = ['_'] * 9
def print_board():
  print(board[0] + '|' + board[1] + '|' + board[2])
  print(board[3] + '|' + board[4] + '|' + board[5])
  print(board[6] + '|' + board[7] + '|' + board[8])
  
print_board()

print('Welcome to tic tac toe!')

player1=input('player 1. Choose either X or 0')
player2=''

while player1!='X' or '0':
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



winner=0

def winner_check():

  global winner

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

  elif goes==8:
    print('It is a draw!')
    winner=winner+1
    
chosenpositions=['']

goes=0

while winner!=1:

  while True:
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    else:
      break


  while int(x)>8:
    print('Only below 8 please')
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    if int(x)>8:
      continue
    else:
      x=int(x)
      break


  while x in chosenpositions:
    print('that position has been taken! try again')
    try:
      x=int(input('Player 1 ('+str(player1)+') pick a number from 0-8'))
    except ValueError:
      print('That was not a number! Please try again')
      continue
    else:
      x=int(x)
      break
    
  else:
    x=int(x)
    print('You chose, position '+str(x))
    board[x] = player1
    chosenpositions.insert(0,x)
    print_board()
    goes=goes+1
    winner_check()
    if winner==1:
      break

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


