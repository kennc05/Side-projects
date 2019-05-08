print('The grid layout')
print('0|1|2\n3|4|5\n6|7|8')
print('')


board = ['_'] * 9
def print_board():
  print(board[0] + '|' + board[1] + '|' + board[2])
  print(board[3] + '|' + board[4] + '|' + board[5])
  print(board[6] + '|' + board[7] + '|' + board[8])
  
print_board()

#asking for player 1 input

print('Welcome to tic tac toe!')
player1=input('player 1. Choose either X or O')


player2=''


if player1=='X':
  player2='O'
  print('player 2 you are O')
  
if player1=='O':
  player2='X'
  print('player 2 you are X')
  




winner=0

def winner_check():
  if board[0] == 'X' and board[1]=='X' and board[2] == 'X':
     print('player X won!!')
     winner=winner+1

  
  elif board[0] == 'O' and board[1]== 'O' and board[2] == 'O':
    print('player O won!!')
    winner=winner+1

  elif board[3] == 'X' and board[4]== 'X' and board[5] == 'X':
    print('player X won!!')
    winner=winner+1

  elif board[3] == 'O' and board[4]== 'O' and board[5] == 'O':
    print('player O won!!')
    winner=winner+1
    
  elif board[6] == 'X' and board[7]== 'X' and board[8] == 'X':
    print('player X won!!')
    winner=winner+1

  elif board[6] == 'O' and board[7]== 'O' and board[8] == 'O':
    print('player O won!!')
    winner=winner+1 

  elif board[0] == 'X' and board[3]== 'X' and board[6] == 'X':
    print('player X won!!')
    winner=winner+1 

  elif board[0] == 'O' and board[3]== 'O' and board[6] == 'O':
    print('player O won!!')
    winner=winner+1 

  elif board[1] == 'X' and board[4]== 'X' and board[7] == 'X':
      print('player X won!!')
      winner=winner+1    

  elif board[1] == 'O' and board[4]== 'O' and board[7] == 'O':
      print('player O won!!')
      winner=winner+1   

  elif board[2] == 'X' and board[5]== 'X' and board[8] == 'X':
      print('player X won!!')
      winner=winner+1       

  elif board[2] == 'O' and board[5]== 'X' and board[8] == 'O':
      print('player O won!!')
      winner=winner+1   

  elif board[2] == 'X' and board[4]== 'X' and board[6] == 'X':
      print('player X won!!')
      winner=winner+1   

  elif board[2] == 'O' and board[4]== 'O' and board[6] == 'O':
      print('player O won!!')
      winner=winner+1  

  elif board[0] == 'X' and board[4]== 'X' and board[8] == 'X':
      print('player X won!!')
      winner=winner+1  

  elif board[0] == 'O' and board[4]== 'O' and board[8] == 'O':
      print('player O won!!')
      winner=winner+1      


while winner!=1:
  
  winner_check()
  x = input('Player 1 pick a number from 0-8')
  x = int(x)
  board[x] = player1
  print_board()
  
  winner_check()
  y = input('Player 2 pick a number from 0-8')
  y = int(y)
  board[y] = player2
  print_board()
  



