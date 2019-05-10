#CHANGES -V4.0#
#Made it negative to touch a threat
#Made it cost -10 to destroy a threat
#Added requirement that to complete level all threats/ gold has to be collected
#If balance was negative, game would end
#Outputs total wealth at end of the game

import turtle
import math
import random


#creating a new screen
window = turtle.Screen()

#set backbground to black
window.bgcolor("black")

#Name window 'Jason's magical maze game'
window.title("Jason's magical maze game")

#How big the window should be 
window.setup(700,700)

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
        self.gold = 1000 #set the value of the gold
        self.goto(x, y)

    #defining destroying the threat
    def destroy_key(self):
        global threatscaught
        window.onkey(None, "space")
        self.goto(2000, 2000)
        self.hideturtle()
        player.gold = player.gold + threat.gold
        print ("BOOM! Threat removed! PLayer gold is now: " +(str(player.gold)))
        threatscaught = threatscaught + 1
        


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
        print("Conratulations you have reached the end!")
        print ("Final player gold is: " +(str(player.gold)))
        player.goto(player_coords)
        window.tracer(0)
        turtle.clear
        turtle.bye()

    #Defining the routing when the game has not ended, but player attempts to end it
    def not_ended(self):
        print("Not eligible to finish yet! Please get the following. Wealth lost -10")
        print("Total treasure: "+str(treasurecount)+"| Total caught: "+str(treasurecaught))
        print("Total threats: "+str(threatcount)+"| Total caught: "+str(threatscaught))
        player.gold = player.gold - 10
        print ("Player gold is now: " +(str(player.gold)))
        print("Returning to start point")
        player.goto(player_coords)


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

#choosing a random number between 1,3 to choose the Maze to open
txtfilenumber=random.randint(1,3)
filename=str(txtfilenumber)+".txt"

with open(filename, "r") as f:
    level0 = []
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

window.tracer(0) #stops screen update


#Loop that updates everytime the player moves
while True:
    if player.gold<0:#Negative wealth balance
        print("Negative wealth! Game over.")
        print ("Final player gold is: " +(str(player.gold)))
        break #ends the loops and ends the game
        
        
    for treasure in treasures_coords:#for every treasure in the treasures list
        if player.touched_object(treasure):
            player.gold = player.gold + treasure.gold
            print ("Player gold is now: " +(str(player.gold)))
            treasures_coords.remove(treasure) #remove that treasure from the treasures list
            treasure.destroy()
            treasurecaught = treasurecaught + 1

    for threat in threats_coords:#for every threat in the treasures list
        if player.touched_object(threat):#If player has touched a threat, walth is reduced by -10, and also using a weapon on the threat reduces wealth by -10 
            print("Ouch! Threat touched, wealth reduced by -10")
            player.gold = player.gold - 10 
            print ("Player gold is now: " +(str(player.gold)))
            window.onkey(threat.destroy_key, "space")
            threats_coords.remove(threat)

         
    for end in endpoint_coords:#for the one enpoint in the endpoint list
        if player.touched_object(end): #if player has touched the end point
            if treasurecaught == treasurecount and threatscaught == threatcount:
                end.turtle_end()
                
        
            else:
                end.not_ended()
    #update the window with any changes
    window.update()
#end the program
turtle.bye()
