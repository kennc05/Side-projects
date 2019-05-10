##CHANGES -V2.0-##
#Changed background colour from black to green
#Reorganised code
#Renamed pen to wall to make it clearer

#importing the turtle library to be able to draw on the screen
import turtle

#import the math module to be able to carry out calculations
import math

####LEVELS SETUP####

#levels will contain the levels playable by the maze    
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

#add the first level to the list
levels.append(level0)

#### MAZE WINDOW SETUP #####

#creating a new screen and setting it as a window variable
window = turtle.Screen()

#set backbground to black
window.bgcolor("green")

#Name window A mAze game
window.title("Jason's Maze game")

#setting window size to 700x700
window.setup(700,700)

####MAZE GAME CLASSES SETUP ####

#A class is a definition of an object - defines its behaviour + properties
#Defining a new class called Wall that will define the characteristics of a wall 
class Wall(turtle.Turtle):
    def __init__(self): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise the class 
        self.shape("square") #shape of what the wall should be
        self.color("blue") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed


#Defining a new class called Player that will define the characteristics of the player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

    #defining the movement of the player - going up, down, left, right
    #Going up: Vertically is +positive | Going down: Verticall is -negative | Going right: Horizontall is +positive |Going left: Horizontally is -negative
    def go_up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24

        if (move_x, move_y) not in wall_coords: #if where the player will move to a place that is not in the wall coords list, then it will move
            self.goto(move_x, move_y) 
        
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

    #defining a new class that would check if the player has reached the end point
    def reached_end(self,other): #other would be the player
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False

#creating a new End class, that creates the shape that the player will need to go to to reach the end
class End(turtle.Turtle):
    def __init__(self, x, y): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("circle") #shape of the person
        self.color("red") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed
        self.goto(x, y)


#### MAZE DRAWING SETUP ####
#Create routing draw_maze, where the maze will be drawn up in a window

def draw_maze(level): #the levels list
    for y in range(len(level)): #for y coords
        for x in range(len(level[y])):
            #Get the character at each x,y coord
            #Y goes first as the maze is stored in a LIST, so goes line by line, vertically
            character = level[y][x]
            #Go through the list and note down all coordinates for each character
            x_coords = -288 + (x * 24) #24 is for each bl ock accross 
            y_coords = 288 - (y * 24)

            finalcoords = (x_coords, y_coords)

            #Within the level list, an X represents a wall, therefore calls on the wall class to draw a square
            if character == "X":
                wall.goto(finalcoords)
                wall.stamp()
                
                #also add the coords to the wall_coords list to be saved later
                wall_coords.append((finalcoords))

            if character == "P":
                player.goto(finalcoords) #set the player to start where P is located

            #E within the levels list represents the end point, once identified, it will add it's coordinates to the End class
            if character == "E":
                endpointcoord.append(End(x_coords, y_coords))


## MAZE WINDOW SETUP ##\

#creating a new screen and setting it as a window variable
window = turtle.Screen()

#set backbground to black
window.bgcolor("green")

#Name window A mAze game
window.title("Jason's Maze game")

#setting window size to 700x700
window.setup(700,700)


#A class is a definition of an object - defines its behaviour + properties
#Defining a new class called Wall that will define the characteristics of a wall 
class Wall(turtle.Turtle):
    def __init__(self): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise the class 
        self.shape("square") #shape of what the wall should be
        self.color("blue") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed


#Defining a new class called Player that will define the characteristics of the player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

    #defining the movement of the player - going up, down, left, right
    #Going up: Vertically is +positive | Going down: Verticall is -negative | Going right: Horizontall is +positive |Going left: Horizontally is -negative
    def go_up(self):
        move_x = player.xcor()
        move_y = player.ycor() + 24

        if (move_x, move_y) not in wall_coords: #if where the player will move to a place that is not in the wall coords list, then it will move
            self.goto(move_x, move_y) 
        
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

    #defining a new class that would check if the player has reached the end point
    def reached_end(self,other): #other would be the player
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False

#creating a new End class, that creates the shape that the player will need to go to to reach the end
class End(turtle.Turtle):
    def __init__(self, x, y): #referring to the object that will be called on
        turtle.Turtle.__init__(self) #initialise pen
        self.shape("circle") #shape of the person
        self.color("red") #color of the person
        self.penup() #By default, a turtle leaves a trail behind, we don't want this
        self.speed(0) #Animation speed
        self.goto(x, y)

#Call upon the classes that I defined earlier                      
wall = Wall()
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


while True:
    window.update() #update the screen
    for end in endpointcoord:
        if player.reached_end(end):
            print("Conratulations you have reached the end!")
            turtle.bye()

    window.update
