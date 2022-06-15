import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-(self.screen.window_width() // 2 - 20), self.screen.window_width() // 2 - 20)
        random_y = random.randint(-(self.screen.window_width() // 2 - 20), self.screen.window_width() // 2 - 20)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-(self.screen.window_width() // 2 - 20), self.screen.window_width() // 2 - 20)
        random_y = random.randint(-(self.screen.window_width() // 2 - 20), self.screen.window_width() // 2 - 20)
        self.goto(random_x, random_y)

