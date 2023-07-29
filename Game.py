import math
import turtle
import random
import os

win=turtle.Screen()
win.bgcolor("black")
win.title("Basic Game Using Classes")
win.bgpic("space.gif")
win.tracer(0)

win.register_shape("alien.gif")
win.register_shape("stone.gif")
win.register_shape("rocket.gif")

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color("white")
        self.hideturtle()
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(300,-300)
        self.goto(300,300)
        self.goto(-300,300)
        self.goto(-300,-300)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.score=0
        self.lives=5
        self.goto(-270,310)
        self.write("Score: 0 Lives: 5",False,align="center",font=("ariel",14,"normal"))

    def update_score(self):
        self.clear()
        self.write("Score: {} Lives: {}".format(self.score,self.lives),False,align="center",font=("ariel",14,"normal"))

    def change_score(self,points):
        self.score+=points
        self.update_score()
    def change_lives(self):
        self.lives-=1
        self.update_score()
        

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("rocket.gif")
        self.color("white")
        self.speed=1

    def move(self):
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)

    def move_left(self):
        self.left(45)

    def move_right(self):
        self.right(45)

    def speedup(self):
        self.speed+=1

    def clear_player(self):
        self.setposition(10000,10000)

class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("alien.gif")
        self.color("green")
        self.speed(0)
        self.speed=5
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

    def clear_ball(self):
        self.hideturtle()

class Stone(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("stone.gif")
        self.color("green")
        self.speed(0)
        self.speed=5
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)
    
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

    def clear_stone(self):
        self.hideturtle()


def play_sound(sound_file,time=0):
        os.system("afplay {}&".format(sound_file))
        if time>0:
            turtle.ontimer(lambda:play_sound(sound_file),t=int(time*1000))
        

def iscollision(t1,t2):
    a=t1.xcor()-t2.xcor()
    b=t1.ycor()-t2.ycor()
    distance= math.sqrt(a**2 + b**2)
    if distance<30:
        return True
    else:
        return False
balls=[]
for _ in range(6):
    balls.append(Ball())
stones=[]
for _ in range(6):
    stones.append(Stone())



player=Player()
border=Border()
border.draw_border()
score=Game()

turtle.listen()
turtle.onkeypress(player.move_left,"Left")
turtle.onkeypress(player.move_right,"Right")
turtle.onkeypress(player.speedup,"Up")
play_sound("")



while True:
    win.update()
    player.move()
    for ball in balls:
        ball.move()
        if iscollision(player,ball):
            ball.jump()
            score.change_score(10)
            play_sound("explosion.wav")

    for stone in stones:
        stone.move()
        if iscollision(player,stone):
            stone.jump()
            score.change_score(-10)
            score.change_lives()
            play_sound("explosion.wav")
    
    




