from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move(self):
        """
        In order to move/turn the snake, we want to move each segments to the pos of the previous segments.
        I.e. when the head (1st segment) of the snake move from (0,0) to (20, 0).
        then the 2nd segments new pos is (0,0)
        We will loop from the tail to the head.
        """

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        # self.segments[0].forward(MOVE_DIST)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        # self.segments[0].forward(MOVE_DIST)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        # self.segments[0].forward(MOVE_DIST)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        # self.segments[0].forward(MOVE_DIST)
