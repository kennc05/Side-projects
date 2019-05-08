##CHANGES -V3.0-##
#Added the ability to import a level from a .txt file
#Added some threates
#Added some treasure

import turtle
import math
import random
#creating a new screen
window = turtle.Screen()

#set backbground to black
window.bgcolor("black")

#Name window A mAze game
window.title("A Maze game")

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
        self.speed(0) #Animation speed

#Defining a new class for the player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 0 #defining the gold player has 

    #defining the movement of the player
    def go_up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24

        if (move_x, move_y) not in wall_coords: #if where the player will move to is not in the wall coords list, then it will move
            self.goto(move_x, move_y) #Y cor is vertical so + is up
        
    def go_down(self):
        move_x = player.xcor()
        move_y = player.ycor() - 24

        if (move_x, move_y) not in wall_coords:
            self.goto(move_x, move_y)

    #Going left is negative
    def go_left(self):
        move_x = player.xcor() - 24
        move_y = player.ycor() 

        if (move_x, move_y) not in wall_coords:
            self.goto(move_x, move_y)

    #Going right is positive 
    def go_right(self):
        move_x = player.xcor() + 24
        move_y = player.ycor() 

        if (move_x, move_y) not in wall_coords:
            self.goto(move_x, move_y)        


    def touched_object(self, other): #other would be the object concerned
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

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
        window.onkey(None, "space")
        self.goto(2000, 2000)
        self.hideturtle()
        player.gold = player.gold + threat.gold
        print ("Threat removed! PLayer gold is now: " +(str(player.gold)))
        



#Defining a new End point class        
class End(turtle.Turtle):
    def __init__(self, x, y): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("circle") #shape of the person
        self.color("green") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed
        self.goto(x, y)
        self.hideturtle()


    
levels = [""]

#defining the first level
#grid size is 25x25 in text
#x -> horizxontal
#y ^ vertical 

with open("1.txt", "r") as f:
    level0 = []
    for line in f:
        level0.append(line)
    print (level0)

levels.append(level0)

print (levels)

def draw_maze(level): #the levels list
    for y in range(len(level)): #for y coords
        for x in range(len(level[y])):
            #Get the characgter at each x,y coord
            #Y goes first as the maze is stored in a LIST, so goes line by line, vertically
            character = level[y][x]
            #Go through the list and note down all coordinates for each character
            x_coords = -288 + (x * 24) #24 is for each bl ock accross 
            y_coords = 288 - (y * 24)

            finalcoords = (x_coords, y_coords)

            #If an X is down, draw a block in the maze
            if character == "X":
                walls.goto(finalcoords)
                walls.stamp()

                #also add the coords to the wall_coords list to be saved later
                wall_coords.append((finalcoords))

            if character == "G":
                treasures_coords.append(Treasure(x_coords, y_coords)) #add the coordinates to the treasure list and also assign the coordinates to the treasure class
                print("TREASURE: " +str(treasures_coords))

            if character == "T":
                threats_coords.append(Threat(x_coords, y_coords)) #add the coordinates to the treasure list and also assign the coordinates to the treasure class
                print("THREAT: " +str(threats_coords))
                
            if character == "E":
                endpoint_coords.append(End(x_coords, y_coords)) #same as above but to the enpointcoord list and assign the coordinates to the End class
                print("ENDPOINT: " +str(endpoint_coords))

            if character == " ":
                emptyspace_coords.append([x_coords, y_coords])
                print("EMPTY SPACE: " +str(emptyspace_coords))

walls = Walls()

player = Player()

#create a list calles walls so we know the coordinates of the walls so player cant walk into it
wall_coords = []
endpoint_coords = []
treasures_coords = []
threats_coords = []
emptyspace_coords =[]

#Setup the level


draw_maze(levels[1])

player_coords= random.choice(emptyspace_coords)
player.goto(player_coords)
print("Player allocated to coords: " +str(player_coords))

#Keyboard controls
window.listen()
window.onkey(player.go_left,"Left") #left arrow
window.onkey(player.go_right,"Right") #right arrow
window.onkey(player.go_up,"Up") #Up key
window.onkey(player.go_down,"Down") #Down key

window.tracer(0) #steps screen update


while True:
    for treasure in treasures_coords:#for every treasure in the treasures list
        if player.touched_object(treasure):
            player.gold = player.gold + treasure.gold
            print ("PLayer gold is now: " +(str(player.gold)))
            treasures_coords.remove(treasure) #remove that treasure from the treasures list
            treasure.destroy()

    for threat in threats_coords:#for every threat in the treasures lis
        if player.touched_object(threat):
            window.onkey(threat.destroy_key, "space")
            threats_coords.remove(threat)

         
    for end in endpoint_coords:
        if player.touched_object(end):
            print("Conratulations you have reached the end!")
            turtle.bye()


    window.update()
