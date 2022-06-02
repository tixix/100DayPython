import random
import turtle as t

timmy_the_turtle = t.Turtle()
MAX_ANKLE = 360
t.colormode(255)


######## Challenge 1 - Draw a Square ############
def draw_square(size):
    ankle = 90
    for _ in range(4):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.right(ankle)


def dashed_line(length_of_line, numbers_of_dashed_lines):
    for _ in range(numbers_of_dashed_lines):
        timmy_the_turtle.forward(length_of_line)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(length_of_line)
        timmy_the_turtle.pendown()


def draw_all_shapes(ankles_to_start_with, ankles_to_end_with):
    t.colormode(255)
    number = 0
    while number < ankles_to_end_with:
        timmy_the_turtle.pencolor(random_color())
        for _ in range(ankles_to_start_with + number, (ankles_to_start_with + number) * 2):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(MAX_ANKLE / (ankles_to_start_with + number))
        number += 1


def draw_random_walk():
    timmy_the_turtle.shape('arrow')
    timmy_the_turtle.pensize(5)
    timmy_the_turtle.speed(10)
    while True:
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.setheading(random.randrange(0, 360, 90))
        timmy_the_turtle.forward(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(radius, size_of_gap):
    timmy_the_turtle.speed(0)
    for i in range(0,360,size_of_gap):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(radius)
        timmy_the_turtle.setheading(i)


# draw_random_walk()
while True:
    draw_spirograph(100,5)
screen = t.Screen()

screen.exitonclick()
