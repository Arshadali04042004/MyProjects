import turtle
import time
import random
 

delay = 0.1
score = 0
highScore = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"

food = turtle.Turtle()
color = random.choice(['red','blue','green'])
shapes = random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.penup()
food.goto(0,100)

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('white')
pen.penup()
pen.goto(0,250)
pen.write("Score : 0 High Score : 0",align="center",font=("arial",24,"bold"))

def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction == "up":
        head.direction = "down"
def goleft():
    if head.direction == "right":
        head.direction = "left"
def goright():
    if head.direction == "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(goup,'w')
wn.onkeypress(godown,'s')
wn.onkeypress(goleft,'d')
wn.onkeypress(goright,'a')

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<=290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red','blue','green'])
        shapes = random.choice(['square','circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score :{}".format(score,highScore),align="center",font=("arial",24,"bold"))
    if head.distance(food)<20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("grey")
        newSegment.penup()
        segment.append(newSegment)

        delay -= 0.001
        score += 10
        
        if score > highScore:
            highScore = score
        pen.clear()
        pen.write("Score : {} High Score :{}".format(score,highScore),align="center",font=("arial",24,"bold"))
    
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Stop"
            colors = random.choice(['red','green','blue'])
            shapes = random.choice(['square','circle'])
            for segment in segments:
               segment.goto(1000,1000)
            segment.clear()

            score = 0
            delay =0.1
            pen.clear()
            pen.write("Score : {} High Score :{}".format(score,highScore),align="center",font=("arial",24,"bold"))
        time.sleep(delay)



wn.mainloop()