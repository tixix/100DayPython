import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()

SCREEN_COLOR = 'black'
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
# r_paddle.speed('fastest')
l_paddle = Paddle((-350, 0))
# l_paddle.speed('fastest')
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # print(ball.distance(r_paddle))

    # detect collision with the top and bottom border
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # pass right paddle
    if 380 < ball.xcor():
        ball.reset_position()
        scoreboard.l_point()

    # pass left paddle
    if -380 > ball.xcor():
        ball.reset_position()
        scoreboard.r_point()
    # game_is_on = False


screen.exitonclick()
