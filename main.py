from turtle import Screen, Turtle
from paddle import Paddle
import random
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("The Breakout Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

# ---------Creating Box------
COLORS = ["#C2185B", "#7B1FA2", "#512DA8", "#1976D2", "#0097A7", "#388E3C", "#AFB42B", "#F57C00", "#5D4037", "#78909C"]
all_box = []
x_coordinate = -370
y_coordinate = 150

for index in range(3):
    for number in range(13):
        new_box = Turtle(shape="square")
        new_box.shapesize(stretch_wid=2, stretch_len=3)
        new_box.color(random.choice(COLORS))
        new_box.penup()
        all_box.append(new_box)
        new_box.goto(x_coordinate, y_coordinate)
        x_coordinate += 61
    x_coordinate = -370
    y_coordinate -= 41

# --------paddle------
paddle = Paddle()
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

# --------Ball-------
ball = Ball()

# ------Score----
score = Scoreboard()
number_of_out = 0

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with box
    for box in all_box:
        if box.distance(ball) < 50:
            ball.bounce_y()
            box.goto(1000, 1000)
            all_box.remove(box)
            score.result()

    # detect collision with the wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # detect collision with the paddle
    if (paddle.xcor() - 60) < ball.xcor() < (paddle.xcor() + 60) and ball.ycor() < -250:
        ball.bounce_y()

    # detect when ball misses the paddle
    if ball.ycor() < -300:
        number_of_out += 1
        if number_of_out == 5:
            score.game_over()
            is_game_on = False

        ball.reset_position()


screen.exitonclick()
