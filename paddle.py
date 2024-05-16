from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -270)

    def go_right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 40
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())
