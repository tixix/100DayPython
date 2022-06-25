import random
from turtle import Turtle

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.speed('slowest')

    def create_ball(self):
        self.penup()
        self.ht()
        self.shapesize()
        self.shape('circle')
        self.color('white')
        self.home()
        self.st()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

