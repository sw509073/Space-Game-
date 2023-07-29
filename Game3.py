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
win.register_shape("bigstone.gif")

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
        self.color("yellow")
        self.speed(0)
        self.score=0
        self.lives=5
        self.level=1
        self.goto(0,310)
        self.write("Score: 0 Lives: 5 Level: 1",False,align="center",font=("ariel",20,"normal"))

    def update_score(self):
        self.clear()
        self.write("Score: {} Lives: {} Level: {}".format(self.score,self.lives,self.level),False,align="center",font=("ariel",20,"normal"))

    def change_score(self,points):
        self.score+=points
        self.update_score()
    def change_lives(self,liv):
        self.lives-=liv
        self.update_score()
    def change_level(self,lel):
        self.level+=lel
        self.update_score()
        

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("rocket.gif")
        self.color("white")
        self.speed=1
        self.setheading(90)

    def move(self):
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)

    def move_left(self):
        self.left(30)

    def move_right(self):
        self.right(30)

    def speedup(self):
        self.speed+=1

    def speedown(self):
        self.speed-=1

    def clear_player(self):
        self.setposition(10000,10000)

    def show_player(self):
        self.setposition(0,0)

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

    def show_ball(self):
        self.showturtle()

class Bigball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("bigstone.gif")
        self.color("green")
        self.speed(0)
        self.speed=5
        self.goto(random.randint(-250,250),random.randint(-250,-240))
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor()<-290:
            self.left(60)
        if self.ycor()>290 or self.ycor()<-290:
            self.left(60)
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

    def clear_Bigball(self):
        self.hideturtle()

    def show_Bigball(self):
        self.showturtle()

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

    def show_stone(self):
        self.showturtle()


def play_sound(sound_file,time=0):
        os.system("afplay {}&".format(sound_file))
        if time>0:
            turtle.ontimer(lambda:play_sound(sound_file),t=int(time*1000))
        

def iscollision(t1,t2):
    a=t1.xcor()-t2.xcor()
    b=t1.ycor()-t2.ycor()
    distance= math.sqrt(a**2 + b**2)
    if distance<40:
        return True
    else:
        return False
balls=[]
for _ in range(6):
    balls.append(Ball())

stones=[]
for _ in range(6):
    stones.append(Stone())

bigballs=[]
for _ in range(1):
    bigballs.append(Bigball())


game_state="start"
def start_game():
    global game_state
    game_state="game"

score=Game()
player=Player()
border=Border()
border.draw_border()


turtle.listen()
turtle.onkeypress(player.move_left,"Left")
turtle.onkeypress(player.move_right,"Right")
turtle.onkeypress(player.speedup,"Up")
turtle.onkeypress(player.speedown,"Down")
turtle.onkeypress(start_game,"space")

play_sound("",44)

while True:
    win.update()
    
    for ball in balls:
        ball.move()
        if iscollision(player,ball):
            ball.jump()
            score.change_score(20)
            play_sound("lose.wav")

    for stone in stones:
        stone.move()
        if iscollision(player,stone):
            stone.jump()
            score.change_score(-10)
            score.change_lives(1)
            play_sound("explosion.wav")

    for bigball in bigballs:
        bigball.move()
        if iscollision(player,bigball):
            play_sound("explosion.wav")
            game_state="over"

    if score.score>100 and score.level==1:
        score.change_lives(-1)
        score.change_level(1)
        for _ in range(2):
            balls.append(Ball())

    if score.score>200 and score.level==2:
        score.change_lives(-1)
        score.change_level(1)
        for _ in range(2):
            stones.append(Stone())
        for _ in range(1):
            bigballs.append(Bigball())

    if score.score>300 and score.level==3:
        score.change_lives(-1)
        score.change_level(1)
        for _ in range(2):
            balls.append(Ball())

    if score.score>400 and score.level==4:
        score.change_lives(-1)
        score.change_level(1)
        for _ in range(2):
            stones.append(Stone())
        for _ in range(1):
            bigballs.append(Bigball())

    if score.score>500 and score.level==5:
        game_state="win" 
    
    if game_state=="start":
        
        for stone in stones:
            stone.clear_stone()
        for ball in balls:
            ball.clear_ball()
        for bigball in bigballs:
            bigball.clear_Bigball()

        win.bgpic("start.gif")

    if game_state=="game":
        player.move()

        for stone in stones:
            stone.show_stone()
        for ball in balls:
            ball.show_ball()
        for bigball in bigballs:
            bigball.show_Bigball()
        win.bgpic("space.gif")
       
        if score.lives<0:
            game_state="over"

        if score.level==2:
            win.bgpic("level2.gif")
        if score.level==3:
            win.bgpic("level3.gif")
        if score.level==4:
            win.bgpic("level4.gif")
        if score.level==5:
            win.bgpic("level5.gif")

    if game_state=="win":
        for stone in stones:
            stone.clear_stone()
        for ball in balls:
            ball.clear_ball()
        for bigball in bigballs:
            bigball.clear_Bigball()
        win.bgpic("win.gif")

    if game_state=="over":

        for stone in stones:
            stone.clear_stone()
        for ball in balls:
            ball.clear_ball()
        for bigball in bigballs:
            bigball.clear_Bigball()
        win.bgpic("gameover.gif")