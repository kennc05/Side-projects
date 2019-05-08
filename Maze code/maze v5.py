#CHANGES -V5.0#
#Added time to count how long a message will be displayed for 
#Added text to welcome player + announce any event ingame
import turtle
import math
import random
import time


#creating a new screen
window = turtle.Screen()

#How big the window should be 
window.setup(700,700)

#Name window 'Jason's  maze game'
window.title("Jason's maze game")


#set backbground to black
window.bgcolor("white")
turtle.color("black")
print("Welcome message displayed")
turtle.write("Welcome!", align="center", move=True, font=("Arial",20,"bold"))
playername=str(window.textinput("Enter your name", "What is your name?"))
time.sleep(2)
turtle.clear()
print("Player greet and instructions displayed")
turtle.write("Nice to meet you "+playername+"!\n\nHow to play the game: \nMove around with the arrow keys.\nWealth is your total points.You start with 0.\nTreasure which is gold can be collected for 10 points.\nThreats which are red must be defused by pressing SPACEBAR when you are near them!\nYou can get 5 gold when you destroy one.\nYou must destroy all threats and collect all gold before finishing a level!\nIf you become bankrupt with negative points, the game will end.\nHave fun!", align="center", move=True, font=("Arial",15,"normal"))
time.sleep(5)
turtle.clear()
print("Loading level")
turtle.write("Now loading level, please wait...", align="right", move=False, font=("Arial",20,"bold"))
time.sleep(2)
turtle.clear()
window.bgcolor("black")




#A class is a definition of an object - defines its behaviour + properties
#Defining a new class called Walls that will become a turtle that draws walls
class Walls(turtle.Turtle):
    def __init__(self): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("square") #shape of the person
        self.color("white") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(100000000000000000000000000000) #Animation speed

#Defining a new class for the player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 0 #defining the gold player has 

    #Defining the movement of the player

    #going up is a positive y coorindate
    def go_up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24

        if (move_x, move_y) not in wall_coords: #if where the player will move to is not in the wall coords list, then it will move
            self.goto(move_x, move_y) #Y cor is vertical so + is up

    #going down is a negative y coordinate    
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

#Defining a new class for treasure that can be collected in game
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
        if player.near(self):
            self.goto(2000, 2000)
            self.hideturtle()
            player.gold = player.gold + threat.gold
            threats_coords.remove(self)
            print("BOOM! Threat removed! Player wealth is now: " +(str(player.gold)))

        else:
            return

       #Defining a new End point class        
class End(turtle.Turtle):
    def __init__(self, x, y): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("circle") #shape of the person
        self.color("green") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed
        self.goto(x, y)

    #Defining the end routine
    def ended(self):
        turtle.clear()
        turtle.penup()
        turtle.home()
        window.bgcolor("white")
        turtle.color("black")
        turtle.write("Conratulations, "+playername+" you have reached the end!!!!",  align="center", move=True, font=("Arial",30,"bold"))
        time.sleep(10)
        turtle.clear()
        turtle.home
        turtle.write("Final player wealth is: " +(str(player.gold)), align="center", move=True, font=("Arial",15,"normal"))
        time.sleep(10)
        player.goto(player_coords)
        window.tracer(0)
        turtle.clear
        

    #Defining the routing when the game has not ended, but player attempts to end it
    def not_ended(self):
        turtle.clear()
        turtle.penup()
        turtle.home()
        window.bgcolor("white")
        turtle.color("black")
        print("Displayed player attempted to finish early message")
        turtle.write("Not eligible to finish yet! Wealth lost: -10 | Please get the following:", align="center", move=True, font=("Arial",15,"normal"))
        time.sleep(5)
        turtle.clear()
        turtle.home()
        turtle.write("Total treasure: "+str(treasurecount)+" | Total caught: "+str(treasurecaught)+"\nTotal threats: "+str(threatcount)+" | Total caught: "+str(threatscaught), align="center", font=("Arial",15,"normal"))
        player.gold = player.gold - 10
        time.sleep(5)
        turtle.clear()
        turtle.home()
        print("Player wealth is now: " +(str(player.gold)))
        turtle.write("Player wealth is now: " +(str(player.gold))+" \nReturning to start point", align="center", font=("Arial",15,"bold"))
        player.goto(player_coords)
        time.sleep(5)
        turtle.clear()
        window.bgcolor("black")


#defining all of the different counts - self explanatory 
treasurecount = 0
threatcount = 0
treasurecaught = 0
threatscaught = 0


#list that will hold the level imported from the text file
levels = [""]

#defining the first level
#grid size is 25x25 in text
#x -> horizxontal
#y ^ vertical 

#choosing a random number between 1,10 to choose the Maze to open
txtfilenumber=random.randint(1,10)
filename=str(txtfilenumber)+".txt"

with open(filename, "r") as f:
    level0 = [""]
    for line in f:
        level0.append(line)
    print("OPENED FILE: "+filename)

levels.append(level0)


#The routine that defines the actual drawing of the maze
def draw_maze(level): 
    global treasurecount
    global threatcount
    for y in range(len(level)): #for y coords
        for x in range(len(level[y])):
            #Get the characgter at each x,y coord
            #Y goes first as the maze is stored in a LIST, so goes line by line, vertically
            character = level[y][x]
            #Go through the list and note down all coordinates for each character
            x_coords = -288 + (x * 24) #24 is the size for each block accross 
            y_coords = 288 - (y * 24)

            finalcoords = (x_coords, y_coords)

            #Defining what character represents each object in the Maze

            #Definine what character a wall is
            if character == "X":
                walls.goto(finalcoords)
                walls.stamp()

                #also add the coords to the wall_coords list to be saved later
                wall_coords.append((finalcoords))

            #Defining what character a piece of gold is
            if character == "G":
                treasures_coords.append(Treasure(x_coords, y_coords)) #add the coordinates to the treasure list and also assign the coordinates to the treasure class
                treasurecount = treasurecount+1

            #Defining what character a threat is
            if character == "T":
                threats_coords.append(Threat(x_coords, y_coords)) #add the coordinates to the treasure list and also assign the coordinates to the treasure class
                threatcount = threatcount+1
                print("THREAT: "+str(threats_coords))

            #Defining what character the end point is
            if character == "E":
                endpoint_coords.append(End(x_coords, y_coords)) #same as above but to the enpointcoord list and assign the coordinates to the End class
       
            #Defining empty spaces
            if character == " ":
                emptyspace_coords.append([x_coords, y_coords])
      

#Making new variables to call on the classes created earlier
walls = Walls()
player = Player()

#create a list of coordinates for each object defined here: walls, endpoint, treasures, threats, empty spaces
wall_coords = [] #So the player can't walk into walls
endpoint_coords = [] #So the player can go into an endpoint
treasures_coords = [] #So the player can claim treasure
threats_coords = [] #So the player can destroy threats
emptyspace_coords =[] #So the player can randomly spawn in empty spaces



#Setup the level - to draw the maze from the list levels that has been imported from the text file
draw_maze(levels[1])

        
        
    




player_coords= random.choice(emptyspace_coords) #Choose a random coordinate from the empty space list
player.goto(player_coords) #Then go to the coordinate
print("Player allocated to coords: " +str(player_coords)) #Print the result



#Keyboard controls
window.listen()
window.onkey(player.go_left,"Left") #left arrow
window.onkey(player.go_right,"Right") #right arrow
window.onkey(player.go_up,"Up") #Up key
window.onkey(player.go_down,"Down") #Down key


#Loop that updates everytime the player moves
while True:
    window.tracer(0)#stops screen update

    
    if player.gold<0:#Negative wealth balance
        turtle.clear()
        turtle.penup()
        turtle.home()
        window.bgcolor("white")
        turtle.color("black")
        turtle.write("Game over, "+playername+".", align="center", font=("Arial",20,"bold"))
        time.sleep(10)
        turtle.clear()
        turtle.write("Final player wealth is: " +(str(player.gold)), align="center", font=("Arial",15,"normal"))
        time.sleep(10)
        player.goto(player_coords)
        window.tracer(0)
        turtle.clear
        print("Played for "+str(minutes)+" minutes and "+str(seconds)+" seconds")
        break #ends the loops and ends the game
        

    for treasure in treasures_coords:#for every treasure in the treasures list
        if player.touched_object(treasure):
            player.gold = player.gold + treasure.gold
            print ("Player wealth is now: " +(str(player.gold)))
            treasures_coords.remove(treasure) #remove that treasure from the treasures list
            treasure.destroy()
            treasurecaught = treasurecaught + 1

    for threat in threats_coords:#for every threat in the treasures list
        if player.near(threat):#If player is near the threat
            window.onkey(threat.destroy_key, "space")

     
        if player.touched_object(threat):
            print("Ouch! Player wealth reduced by 10")
            player.gold = player.gold - 10
            print ("Player wealth is now: " +(str(player.gold)))
            

         
    for end in endpoint_coords:#for the one enpoint in the endpoint list
        if player.touched_object(end): #if player has touched the end point
            if treasurecaught == treasurecount and threatscaught == threatcount:
                end.ended()
                print("Played for "+str(minutes)+" minutes and "+str(seconds)+" seconds")
                break
                
        
            else:
                end.not_ended()
    #update the window with any changes
    window.update()
#end the program
turtle.bye()
