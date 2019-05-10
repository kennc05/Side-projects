Classes used in the python game

Walls = Defined the characteristics of a wall in the game

Player = Defined the characteristics of a player in the game

Treasure = Defined the characteristics of a treasure in the game

Threat = Defined the characteristics of a threat in the game

End = Defined the end point in the game and what to do when the game was ended early

Routines used in the python game

Player.go_up = Move the player up

Player.go_down = Move the player down

Player.go_left = Move the player left

Player.go_right = Move the player right

Player.touched_object = Outputting TRUE or FALSE if a player has touched an object

Player.near = Outputting TRUE or FALSE if a player is within distance of another object

Player.gold = Contains how much wealth points a player has

Player.touchedthreat = If this turns to 1, the player game is ended instantly

Player.win = If this turns to 1m the player game is ended and congratulations message shown

Threat.destroy_key = When the player presses SPACEBAR near a threat, the threat will be removed and 10 wealth points added to the player

End.ended = Defining the routine for the end message to the player and breaking the loop that checks if conditions have been met to end a game

End.not_ended = Displays the attempted to finish early message to player and reduces player wealth points by 10

Draw_maze = Defining the routine that draws the maze and what characters defined what objects were where

Variables used in the python game

Window = Defines the turtle window in the game

Levels = The list that contains the level that is loaded into the game

Txtfilenumber = Will hold a random number between 1 – 10 for the text file to be opened

Filename = combines the txtfilenumber to .txt to make it into a valid file

Level0 = Defines a list that will be added to the levels list when loading the game

Wall_coords = The list that contains all coordinates of walls in the game

Endpoint_coords = The list that contains the end point within the game

Treasures_coords = The list that contains the coordinates of all treasure in the game

Emptyspace_coords = The list that contains all coordinates of empty space in the game

Treasurecount = Contains how many gold treasures there are

Threatcount = Contains how many threats there are

Treasurecaught = Contains how many items of gold a player has caught

Threatscaught = Contains how many threats a player has destroyed

Player_coords = Contains the randomly selected coordinates from the emptyspace_coords list

