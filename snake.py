import turtle, random

class Snake:
    '''
    Purpose: represents the snake we control in the game
    Instance Variables:
        x, y - represent the location
        vx, vy - represent x and y velocity
        color - color of the snake
        segments- the body of the snake
    Methods:
        constructor- initialize instance Variables
        grow- adds a segment to the snake
        move- moves the Snake
        check_coll - checks to see if the snake is out of bounds or runs into itself
        go_down, go_right, go_left, go_up - direct the snake in the respective direction
    '''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.vx = 30
        self.vy = 0
        self.grow()
    def grow(self):
        block = turtle.Turtle()
        block.speed(0)
        block.color(self.color)
        block.shape('square')
        block.shapesize(1.5,1.5,1)
        block.penup()
        block.setpos(self.x, self.y)
        self.segments.append(block)
    def move(self):
        for i in range(len(self.segments) - 1):
            self.segments[i].setpos(self.segments[i+1].pos())
        self.x += self.vx
        self.y += self.vy
        self.segments[-1].setpos(self.x, self.y)
    def check_coll(self):
        coll = False
        if (self.x <= 0):
            coll = True
        elif (self.x >= 600):
            coll = True
        elif (self.y <= 0):
            coll = True
        elif (self.y >= 600):
            coll = True
        for ele in self.segments[0:-2]:
            if (self.x,self.y) == (ele.pos()):
                coll = True
        return coll
    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_up(self):
        self.vx =0
        self.vy = 30
    def go_left(self):
        self.vx = -30
        self.vy = 0

class Game:
    '''
    Purpose: runs the game and sets up the game board
    Instance Variables:
        player- the player's Snake
        pellet- food pieces across the map
    Methods: gameloop- moves the snake when there is no collision
    '''
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        self.player = Snake(315,315,'green')
        self.pellet = Food()
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.listen()
        turtle.mainloop()




    def gameloop(self):
        if self.player.check_coll() == True:
            turtle.write("Game Over", font=("Arial",45, "normal"))
        else:
            self.player.move()
            self.pellet.eaten(self.player)
            turtle.ontimer(self.gameloop, 200)

class Food:
    '''
    Purpose: represent food pellets that grow the Snake
    Instance Variables:
        x,y - represent pellet location
    Methods:
        eaten- determine whether or not the snake is eating a pellet and if it is, the pellet disappears and reappears elsewhere
        initialize- places the first pellet
        place- places a pellet
    '''
    def __init__(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.initialize()
        self.place()
    def eaten(self, other):
        if (self.x == other.x) and (self.y == other.y):
            self.x = 15 + 30*random.randint(0,19)
            self.y = 15 + 30*random.randint(0,19)
            self.place()
            other.grow()
    def initialize(self):
        self.pellet = turtle.Turtle()
    def place(self):
        self.pellet.penup()
        self.pellet.setpos(self.x,self.y)
        self.pellet.color('red')
        self.pellet.shape('circle')
        self.pellet.shapesize(1.5,1.5,1)

Game()
