from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):  # 'self.' refers to the object created in the class
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # width = 20, height = 100
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)