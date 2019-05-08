#CHANGES -V8.0#
#loops can now happen if the user wins or loses
#updated messages to user and reworded wealth to wealth points
#changed window size
#added more messages

#IMPORTING the various libraries needed to make this game run
import turtle
import math
import random
import time


#Make the game loop when you lose or win by setting game_lose_loop to true
game_loop = True

while game_loop:
    
    #-----------------SECTION 1------------------#
    #Where the game window and settings are configured
    
    print("Time for a game! Loading configuration..")
    start_time=time.time() #Start the timer count using the time function


    #creating a new screen
    window = turtle.Screen()

    window.clearscreen() #reset window from other games

    #How big the window should be 
    window.setup(1200,700)

    #Name window 'Jason's  maze game'
    window.title("Jason's maze game")


    #set backbground to white
    
    window.bgcolor("white")
    turtle.color("black")
    turtle.clear()
    turtle.home()
    turtle.penup()
    #Various message to the user is displayed here
    print("Welcome message displayed")
    turtle.write("Welcome to the Maze Game!", align="center", font=("Arial",20,"bold"))
    playername=str(window.textinput("Enter your name", "What is your name?"))
    time.sleep(2)
    turtle.clear()
    turtle.home()
    print("Player greet and instructions displayed")
    turtle.write("Nice to meet you "+playername+"!\n\nThe guide to play the game is as follows: \nMove around the maze with the arrow keys on your keyboard.\nWealth is the total number of points you collect throughout the game - You will start with 0.\nYou MUST collect all treasure and destroy all threats before finishing the game!\nTreasure represented as gold in yellow circles are worth 10 wealth points.\nThreats shown in red circles must be destroyed by pressing SPACEBAR on the keyboard when next to them.\nYou will gain 5 wealth points when you destroy a threat.\nThe game will end when you go over a threat without destroying it or going into negative wealth points.\nWhen you attempt to finish the game early, you will lose 10 wealth points.\n\n\nHave fun!",  align="center", move=True, font=("Arial",15,"normal"))
    time.sleep(10)
    turtle.clear()
    turtle.home()
    print("Loading the Maze, plase wait...")
    turtle.write("Loading the Maze, plase wait...", align="center", move=False, font=("Arial",20,"bold"))
    time.sleep(2)
    turtle.clear()

    window.bgcolor("black")

    #background color is then set to black for level generation



    #---------------------SECTION 2-------------------#
    #This section contains the classes: Walls, Player, Threat, Treasure and End
    #Classes are used throughout the game and are referenced to put objects onto the screen
    #These are all components that come togehet to be a part of the Maze
    
    #A class is a definition of an object - defines its behaviour + properties
    #Defining a new class called Walls that will become a turtle that draws walls - it will be a swaure and white
    class Walls(turtle.Turtle):
        def __init__(self): #referring to the object that will be called on
            turtle.Turtle.__init__(self) #initialise pen
            self.shape("square") #shape of the person
            self.color("white") #color of the person
            self.penup() #By default, a turtle leaves a trail behind, we don't want this
            self.speed(1000) #Animation speed

    #Defining a new class for the player that is square and yellow and on screen
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue") 
            self.penup()
            self.speed(0)
            self.gold = 0 #defining the gold player has
            self.touchedthreat = 0 #if this is 1 then the game will end and loop
            self.win = 0 #If this turns to 1 then the game will end and loop

        #Defining the movement of the player##
        #Going up is a positive y coorindate
        def go_up(self):
            move_x = player.xcor()
            move_y = player.ycor() + 24
            #if where the player will move to somewhere that is not a wall, then it will allow them to move
            if (move_x, move_y) not in wall_coords:
                self.goto(move_x, move_y) #Y cor is vertical so + is up

        #Going down is a negative y coordinate    
        def go_down(self):
            move_x = player.xcor()
            move_y = player.ycor() - 24
            if (move_x, move_y) not in wall_coords:
                self.goto(move_x, move_y)

        #Going left is a negative x coordinate
        def go_left(self):
            move_x = player.xcor() - 24
            move_y = player.ycor() 
            if (move_x, move_y) not in wall_coords:
                self.goto(move_x, move_y)

        #Going right is positive x coordinate
        def go_right(self):
            move_x = player.xcor() + 24
            move_y = player.ycor() 
            if (move_x, move_y) not in wall_coords:
                self.goto(move_x, move_y)        

        #Defining what would count as an object being 'touched' by a played
        def touched_object(self, other): #other would be the object concerned such as threat or treasure
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            #if the distance between the two objects is less than 5, then the object has been 'touched' and returns True
            if distance < 5:
                return True
            else:
                return False

        def near(self, other): #other would be the object concerned such as threat or treasure
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )

            #if the distance between the two objects is less than 5, then the object has been 'touched' and returns True
            if distance < 26:
                return True
            else:
                return False

    #Defining a new class for treasure that can be collected in game - it will be circle and gold
    class Treasure(turtle.Turtle):
        def __init__(self, x, y): #referring to the object that will be called on + where we want the treasure to appear
            turtle.Turtle.__init__(self) #initialise pen
            self.shape("circle") #shape of the person
            self.color("gold") #color of the person
            self.penup() #By default, a turtle leaves a trail behind, we don't want this
            self.speed(0) #Animation speed
            self.gold = 10 #set the value of the gold
            self.goto(x, y)

        #Destroying a treasure hides its object and places it out of the screen
        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    class Threat(turtle.Turtle):
        def __init__(self, x, y): #referring to the object that will be called on + where we want the treasure to appear
            turtle.Turtle.__init__(self) #initialise pen
            self.shape("circle") #shape of the person
            self.color("red") #color of the person
            self.penup() #By default, a turtle leaves a trail behind, we don't want this
            self.speed(0) #Animation speed
            self.gold = 5 #set the value of the gold
            self.goto(x, y)

        #defining destroying the threat
        def destroy_key(self):
            global threatscaught
            if player.near(self):
                self.goto(2000, 2000)
                self.hideturtle()
                player.gold = player.gold + threat.gold
                threats_coords.remove(self)
                print("BOOM! Threat removed! Player wealth points are now: " +(str(player.gold)))
                threatscaught = threatscaught + 1
                
            else:
                return

        

    #Defining a new End point class - it will be circle and green       
    class End(turtle.Turtle):
        def __init__(self, x, y): #referring to the object that will be called on
            turtle.Turtle.__init__(self) #initialise pen
            self.shape("circle") #shape of the person
            self.color("green") #color of the person
            self.penup() #By default, a turtle leaves a trail behind, we don't want this
            self.speed(0) #Animation speed
            self.goto(x, y)

        #Defining the end routine - It will display a message to the player to congratulate them that they have won
        def ended(self):
            turtle.clear()
            turtle.penup()
            turtle.home()
            window.bgcolor("white")
            turtle.color("black")
            print("Displayed congratulations message")
            end_time_minutes=round((time.time()-start_time)/60,1)
            end_time_seconds=round(time.time()-start_time,1)
            turtle.write("Congratulations "+playername+"! You have reached the end!\n\nTotal player wealth points: " +(str(player.gold))+"\nTime taken to complete: "+str(end_time_minutes)+" minutes and "+str(end_time_seconds)+" seconds",  align="center", move=True, font=("Arial",20,"bold"))
            time.sleep(10)
            turtle.clear()
            turtle.home()
            player.goto(player_coords)
            turtle.clear
            player.win = player.win + 1 #adding 1 to break the loop and start again

        #Defining the routine when the game has not ended, but when player attempts to end it early - it will inform the player what else they need before they can complete the game
        def not_ended(self):
            turtle.clear()
            turtle.penup()
            turtle.home()
            window.bgcolor("white")
            turtle.color("black")
            print("Displayed player attempted to finish early message")
            turtle.write("You cannot finish yet!\nYou have lost 10 wealth points\n\nPlease ensure that you collect all the treasure and destroy all threats before finishing", align="center", move=True, font=("Arial",20,"bold"))
            player.gold = player.gold - 10
            time.sleep(10)
            turtle.clear()
            turtle.home()
            print("Player wealth points: " +(str(player.gold)))
            turtle.write("Current wealth points: " +(str(player.gold))+"\n\nReturning to start point", align="center", font=("Arial",20,"bold"))
            player.goto(player_coords)
            time.sleep(5)
            turtle.clear()
            window.bgcolor("black")



    ##-----------Section 3--------------------##
    #Maze building and configuration
    
    #list that will hold the level imported from the text file that will be randomly selected
    levels = [""]

    #choosing a random number between 1,10 to choose the Maze to import to the list
    txtfilenumber=random.randint(1,10)
    filename=str(txtfilenumber)+".txt"

    with open(filename, "r") as f:
        level0 = [""]
        for line in f:
            level0.append(line) #add each line from the .txt file to the levels list
        print("OPENED FILE: "+filename)

    levels.append(level0) #adding the .txt file to the levels list
    
    #The routine that defines the actual drawing of the maze
    def draw_maze(level): 
        global treasurecount #reference to the treasurecount variable that is created below
        global threatcount #references to the threatcount variable that is created below
        for y in range(len(level)): #for y coords
            for x in range(len(level[y])):
                #Get the characgter at each x,y coord
                #Y goes first as the maze is stored in a LIST, so goes line by line, vertically
                character = level[y][x]
                #Go through the list and note down all coordinates for each character
                x_coords = -288 + (x * 24) #24 is the size for each block accross 
                y_coords = 288 - (y * 24)

                finalcoords = (x_coords, y_coords) #Combines the current coordinate to one single variable

                ##Defining what character represents each object in the Maze##
                #Define what character a wall is and adding it to the wall list if found
                if character == "X":
                    walls.goto(finalcoords)
                    walls.stamp()
                    wall_coords.append((finalcoords))

                #Defining what character a piece of gold is and adding it to the treasures list if found
                if character == "G":
                    treasures_coords.append(Treasure(x_coords, y_coords)) #add the coordinates to the treasure list and also assign the coordinates to the treasure class
                    treasurecount = treasurecount+1

                #Defining what character a threat is and adding it to the threats list if found
                if character == "T":
                    threats_coords.append(Threat(x_coords, y_coords)) #add the coordinates to the threats list and also assign the coordinates to the threats class
                    threatcount = threatcount+1

                #Defining what character the end point is and adding it to the endpoints list if found
                if character == "E":
                    endpoint_coords.append(End(x_coords, y_coords)) #add the coordinates to the enpointcoord list and assign the coordinates to the End class
           
                #Defining empty spaces and adding it to the emptyspace list if found
                if character == " ":
                    emptyspace_coords.append([x_coords, y_coords])


    ##------------------SECTION 4-------------------##
        
    #Making new variables to call on the classes created earlier
    walls = Walls()
    player = Player()

    #create a list of coordinates for each object defined here: walls, endpoint, treasures, threats, empty spaces
    wall_coords = [] #So the player can't walk into walls
    endpoint_coords = [] #So the player can go into an endpoint
    treasures_coords = [] #So the player can claim treasure
    threats_coords = [] #So the player can destroy threats
    emptyspace_coords =[] #So the player can randomly spawn in empty spaces

    #defining all of the different counts during the game
    treasurecount = 0 #Will count how many gold treasures can be collecxted
    threatcount = 0 #Will count how many threats there are
    treasurecaught = 0 #Will count how much gold a user has taken
    threatscaught = 0 #Will count how many threats a user has destroyed


    #Setup the level - to draw the maze from the list levels that has been imported from the text file
    draw_maze(levels[1])
            
    #Setting and placing the player on the maze once drawn up
    player_coords= random.choice(emptyspace_coords) #Choose a random coordinate from the empty space list
    player.goto(player_coords) #Then go to the coordinate
    print("Player allocated to coords: " +str(player_coords)) #Print the result


    #Keyboard controls
    window.listen()
    window.onkey(player.go_left,"Left") #left arrow
    window.onkey(player.go_right,"Right") #right arrow
    window.onkey(player.go_up,"Up") #Up key
    window.onkey(player.go_down,"Down") #Down key

    



    ##---------SECTION 5----------------––##
    #This section will continuously loop when the player moves to check each condition seen below, the game over routine is also here

    def game_over():
        turtle.clearscreen()
        turtle.penup()
        turtle.home()
        window.bgcolor("white")
        turtle.color("black")
        print("Displayed game over message")
        end_time_minutes=round((time.time()-start_time)/60,1)
        end_time_seconds=round(time.time()-start_time,1)
        turtle.write("Game over, "+playername+"!\n\nTotal wealth points: " +(str(player.gold))+"\nTime taken: "+str(end_time_minutes)+" minutes and "+str(end_time_seconds)+" seconds", align="center", font=("Arial",20,"bold"))
        time.sleep(10)
        turtle.clear()
        turtle.home()
        print("Loading next game..")
        turtle.write("Loading another game...", align="center", font=("Arial",15,"normal"))
        time.sleep(5)

    #Loop that updates everytime the player moves

    while True:

        #If the player gets into a negative balance below 0, then it will say game over and the game will actually loop again
        if player.gold<0:
            time.sleep(5)
            game_over()
            break

        if player.touchedthreat>0:
            turtle.clearscreen()
            turtle.penup()
            turtle.home()
            window.bgcolor("white")
            turtle.write("RIP. You have gone over a threat!", align="center", font=("Arial",20,"bold"))
            time.sleep(5)
            print("Game over with reason message displayed")
            game_over()
            break

            
        if player.win>1:
            break
            
            
        #For every treasure in the treasures list - if the player 'touches' a specific treasure item and it matches the
        #coordinates in the treasures_coords list, then it will get removed and claimed by the user
        #They will also get a wealth gold balance of 10
        
        for treasure in treasures_coords:
            if player.touched_object(treasure):
                player.gold = player.gold + treasure.gold
                print ("Gold picked up. Player wealth points now: " +(str(player.gold)))
                treasures_coords.remove(treasure) #remove that treasure from the treasures list
                treasure.destroy()
                treasurecaught = treasurecaught + 1

        #For every threat in the threats list - if the player goes near or goes onto a specific threat and it matches the
        #coordinates in the threats_coords list, either lose the game straight away or
        #they move away from the threat. If they press 'spacebar' next to a threat then they can destroy the threat anbd gain 5 wealth.
        
        for threat in threats_coords:#for every threat in the treasures list
            if player.near(threat):#If player is near the threat
                window.onkey(threat.destroy_key, "space")

            if player.touched_object(threat):
                player.touchedthreat = player.touchedthreat + 1
                
                    

        #Once the player reaches the end point, there are two possibilities
        #Outcome 1: The user hasn't collected all treasures or destroyed threats. They will be told what is left to collect / destroy abnd be brought back
        #to where they first started
        #Outcome 2: The user has collected everything, and the end routine is performed where their final wealth is displayed and they are congratulated
        for end in endpoint_coords:#for the one enpoint in the endpoint list
            if player.touched_object(end): #if player has touched the end point
                if treasurecaught == treasurecount and threatscaught == threatcount:
                    player.win = player.win + 1
                    end.ended()
                    break #supposed to break out of the loop but it doesn't
                
                
                else:
                    end.not_ended()
                    continue

            
                
        #update the window with any changes
        window.update()

    #end the program
    window.update()
    window.clearscreen()
    print("playing again!!!")
