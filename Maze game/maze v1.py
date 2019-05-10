##CHANGES -V1.0##
#NA - Beginning of the code!

import turtle
import math
#creating a new screen
window = turtle.Screen()

#set backbground to black
window.bgcolor("black")

#Name window A mAze game
window.title("A Maze game")

#How big the window should be 
window.setup(700,700)

#A class is a definition of an object - defines its behaviour + properties
#Defining a new class called Pen that will become a turtle
class Pen(turtle.Turtle):
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


    def reached_end(self,other): #other would be the player
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False
        
class End(turtle.Turtle):
    def __init__(self, x, y): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("circle") #shape of the person
        self.color("red") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed
        self.goto(x, y)


    
levels = [""]

#defining the first level
#grid size is 25x25 in text
#x -> horizxontal
#y ^ vertical 

level0 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXP XXXXX",
"XXXXXXXXXXXXXXXXXX  XXXXX",
"XXXXXXXXXXXXXXXX    XXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXXX         XXXXXXXX",
"XXXXXXXX       XXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX                 ",
"XXXXXXXX                 ",
"XXXXXXXXXXXXXXXXXX  XXXXX",
"XXXXXXXXXXXXXXXXXX  XXXXX",
"XXXXXXXXXXXXXXXXXX  XXXXX",
"XXXXXXXXXXXXXXXXXX  XXXXX",
"   E                XXXXX",
"                    XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

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
                pen.goto(finalcoords)
                pen.stamp()

                #also add the coords to the wall_coords list to be saved later
                wall_coords.append((finalcoords))

            if character == "P":
                player.goto(finalcoords) #set the player to start where P is located

            if character == "E":
                endpointcoord.append(End(x_coords, y_coords))
                       

pen = Pen()

player = Player()

#create a list calles walls so we know the coordinates of the walls so player cant walk into it
wall_coords = []
endpointcoord =[]

#Setup the level
draw_maze(levels[1])


#Keyboard controls
window.listen()
window.onkey(player.go_left,"Left") #left arrow
window.onkey(player.go_right,"Right") #right arrow
window.onkey(player.go_up,"Up") #Up key
window.onkey(player.go_down,"Down") #Down key

window.tracer(0)


while True:
    window.update() #update the screen
    for end in endpointcoord:
        if player.reached_end(end):
            print("Conratulations you have reached the end!")
            turtle.bye()

    window.update
