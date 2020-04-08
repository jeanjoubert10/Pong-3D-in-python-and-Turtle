
import turtle
import random
import os
import math

win = turtle.Screen()
win.setup(1300,1000)
win.tracer(0)
win.listen()

win.register_shape('paddle.gif')
win.register_shape('paddle2.gif')

def setup():
    t = turtle.Turtle()
    t.up()
    t.goto(0,0)
    t.down()
    t.fd(100)

    for i in range(4):
        t.lt(90)
        t.fd(300)
    t.rt(45)
    t.fd(600)
    t.lt(135)


    t.fd(900)
    t.lt(90)
    t.fd(1148)
    t.lt(90)
    t.fd(900)
    t.lt(90)
    t.fd(1148)
    t.lt(90)
    t.fd(900)
    t.goto(100,300)
    t.goto(-200,300)
    t.goto(-200,0)
    t.lt(180)
    t.rt(45)
    t.fd(600)
    t.seth(90)
    t.fd(900)
    t.goto(-200,300)
    t.ht()


class Ball(turtle.Turtle):
    def __init__(self, paddle):
        super().__init__(shape = 'circle')
        self.color('black', 'red')
        self.size = 1
        self.up()
        self.paddle = paddle
        self.vx = 1
        self.vy = -3
        self.list = [-4,-3.5,-3,-2.5, -2, -1, 0, 1, 2, 2.5, 3, 3.5, 4]

        self.shadow = turtle.Turtle()
        self.shadow.shape('circle')
        self.shadow.color('grey')
        self.shadow.shapesize(0.3,1)
        self.shadow.up()
        self.goto(-30,0)

    def move(self):
        if self.ycor()<=0:
            size = 1+abs(self.ycor()/200)
        else:
            size = 1
            
        self.shadow.shapesize(size*0.3,size)
        self.shadow.goto(self.xcor(),self.ycor()-40)
        
        self.goto(self.xcor()+self.vx, self.ycor()+self.vy)
        self.shapesize(size, size)

        if self.ycor()>30:
            self.vy *= -1
            self.vx = random.choice(self.list)
            os.system('afplay bounce.wav&')


        if self.ycor()<-340 and (paddle.xcor()-50 <= self.xcor() <= paddle.xcor()+50) and self.vy<0:
            self.vy *= -1
            self.vx *= -1
            os.system('afplay hit_sound.wav&')

        if self.ycor()<-400:
            self.goto(-50,0)
            self.vx = random.choice(self.list)
            os.system('afplay gong.wav&')

        # Bounce on side walls
        #if self.xcor()>= 100 + (self.ycor()*-1): # Tan (45) = 1
            #self.vx *= -1

        #if self.xcor()<-200 + (self.ycor()):
            #self.vx *= -1
    

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='paddle.gif')
        self.up()
        self.goto(0,-390)

    def move_right(self):
        if self.xcor()<450:
            self.goto(self.xcor()+30, self.ycor())
            if paddle.xcor()>50:
                paddle.shape('paddle2.gif')

    def move_left(self):
        if self.xcor()>-520:
            self.goto(self.xcor()-30, self.ycor())
            if paddle.xcor()<50:
                paddle.shape('paddle.gif')
            
               
setup()

paddle = Paddle()
ball = Ball(paddle)

win.onkey(paddle.move_right, 'Right')
win.onkey(paddle.move_left, 'Left')

while True:
    win.update()
    ball.move()
    
