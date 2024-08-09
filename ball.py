from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 15
        self.y_move = 15
        self.penup()
        self.move_ball()
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move  # Moving ball from current x_cor to an arbitrary amount
        new_y = self.ycor() + self.y_move  # Moving ball from current y_cor to an arbitrary amount
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
