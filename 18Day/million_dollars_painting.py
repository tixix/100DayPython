import random
import turtle as t
import colorgram

timmy_the_turtle = t.Turtle()
timmy_the_turtle.hideturtle()
MAX_ANKLE = 360
SPEED = 'fastest'
t.colormode(255)
timmy_the_turtle.penup()


def define_rgb_colors_image(path_to_image, number_of_colors):
    # Extract 6 colors from an image.
    colors = colorgram.extract(path_to_image, number_of_colors)
    result = []

    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        result.append((r, g, b))
    return result


def draw_spot_painting(size_of_each_dot, number_of_dots_per_row, rows, dist_of_dots):
    timmy_the_turtle.speed(SPEED)
    for row in range(rows):
        for dot in range(number_of_dots_per_row):
            timmy_the_turtle.fd(dist_of_dots)
            timmy_the_turtle.dot(size_of_each_dot, random.choice(define_rgb_colors_image('image/image.jpg', 30)))
        timmy_the_turtle.backward(number_of_dots_per_row * dist_of_dots)  # no change in the turtle’s heading.
        timmy_the_turtle.right(MAX_ANKLE / 4)  # 90 degree turn
        timmy_the_turtle.forward(dist_of_dots)
        timmy_the_turtle.left(MAX_ANKLE / 4)


draw_spot_painting(size_of_each_dot=20, number_of_dots_per_row=20, rows=10, dist_of_dots=30)
screen = t.Screen()
screen.exitonclick()

