
print('Welcome to this game of tic tac toe')

print ('Player 1 is X, Player 2 is O')

print ('player 1, start')

print('    1 2 3 \n a | | | | \n b | | | | \n c | | | |')

position=input('Player 1, choose a position')

if position == '1a':
    print('    1 2 3 \n a |X| | | \n b | | | | \n c | | | |')
    print('Player 2, your turn')
    position=input('Player 2, choose a position')

    if position == '2a':
        print('    1 2 3 \n a |X|O| | \n b | | | | \n c | | | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')

        if position == '3a':
            print('    1 2 3 \n a |X|O|X| \n b | | | | \n c | | | |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')

            if position == '1b':
                print('    1 2 3 \n a |X|O|X| \n b |O| | | \n c | | | |')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')

                if position == '2b':
                    print('    1 2 3 \n a |X|O|X| \n b |O|X| | \n c | | | |')
                    print('Player 1, your turn')
                    position=input('Player 2, choose a position')

                    if position == '3b':
                        print('    1 2 3 \n a |X|O|X| \n b |O|X|O| \n c | | | |')
                        print('Player 1, your turn')
                        position=input('Player 1, choose a position')

                        if position == '1c':
                            print('    1 2 3 \n a |X|O|X| \n b |O|X|O| \n c |X| | |')
                            print('Player 1, your turn')
                            position=input('Player 2, choose a position')
                            
                            if position == '2c':
                                print('    1 2 3 \n a |X|O|X| \n b |O|X|O| \n c |X|O| |')
                                print('Player 1, your turn')
                                position=input('Player 1, choose a position')

                                if position == '3c':
                                    print('    1 2 3 \n a |X|O|X| \n b |O|X|O| \n c |X|O|X|')
                                    print('Player 1, your turn')
                                    print('Player 1 wins!')









                    

            if position == '2b':
                print('    1 2 3 \n a |X|O|X| \n b | |O| | \n c | | | |')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')

            if position == '3b':
                print('    1 2 3 \n a |X|O|X| \n b | | |O| \n c | | | |')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')
                
            if position == '1c':
                print('    1 2 3 \n a |X|O|X| \n b | | | | \n c |O| | |')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')

            if position == '2c':
                print('    1 2 3 \n a |X|O|X| \n b | | | | \n c | |O| |')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')               
                
            if position == '3c':
                print('    1 2 3 \n a |X|O|X| \n b | | | | \n c | | |O|')
                print('Player 1, your turn')
                position=input('Player 1, choose a position')













                

        if position == '1b':
            print('    1 2 3 \n a |X|O| | \n b |X| | | \n c | | | |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')
            
        if position == '2b':
            print('    1 2 3 \n a |X|O| | \n b | |X| | \n c | | | |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')
        
        if position == '3b':
            print('    1 2 3 \n a |X|O| | \n b | | |X| \n c | | | |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')
            
        if position == '1c':
            print('    1 2 3 \n a |X|O| | \n b | | | | \n c |X| | |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')
            
        if position == '2c':
            print('    1 2 3 \n a |X|O| | \n b | | | | \n c | |X| |')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')

        if position == '3c':
            print('    1 2 3 \n a |X|O| | \n b | | | | \n c | | |X|')
            print('Player 1, your turn')
            position=input('Player 2, choose a position')
            











    if position == '3a':
        print('    1 2 3 \n a |X| |O| \n b | | | | \n c | | | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        
        
    if position == '1b':
        print('    1 2 3 \n a |X| | | \n b |O| | | \n c | | | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        
        
    if position == '2b':
        print('    1 2 3 \n a |X| | | \n b | |O| | \n c | | | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        

    if position == '3b':
        print('    1 2 3 \n a |X| | | \n b | | |O| \n c | | | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        
        
    if position == '1c':
        print('    1 2 3 \n a |X| | | \n b | | | | \n c |O| | |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        
    if position == '2c':
        print('    1 2 3 \n a |X| | | \n b | | | | \n c | |O| |')
        print('Player 1, your turn')
        position=input('Player 1, choose a position')
        
    if position == '3c':
        print('    1 2 3 \n a |X| | | \n b | | | | \n c | | |O|')
        print('Player 2, your turn')
        position=input('Player 2, choose a position')




        
            
if position == '1b':
    print('    1 2 3 \n a | |X| | \n b | | | | \n c | | | |')

if position == '1c':
    print('    1 2 3 \n a | | |X| \n b | | | | \n c | | | |')

if position == '2a':
    print('    1 2 3 \n a | | | | \n b |X| | | \n c | | | |')

if position == '2b':
    print('    1 2 3 \n a | | | | \n b | |X| | \n c | | | |')
    
if position == '2b':
    print('    1 2 3 \n a | | | | \n b | | |X| \n c | | | |')

if position == '3a':
    print('    1 2 3 \n a | | | | \n b | | | | \n c |X| | |')

if position == '3b':
    print('    1 2 3 \n a | | | | \n b | | | | \n c | |X| |')

if position == '3b':
    print('    1 2 3 \n a | | | | \n b | | | | \n c | | |X|')
