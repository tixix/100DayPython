from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.penup()
        self.ht()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.st()

    def up(self):
        if self.ycor() < self.screen.window_height() / 2 - 60:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -(self.screen.window_height() / 2 - 60):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
