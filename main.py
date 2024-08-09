from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# height = 600, width = 800

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

""" Controls screen output and display """

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
""" 
- Putting the right and left paddle at a given position, filling out the 'position' parameter from the paddle class
- Creating a ball object from the 'Ball' class to carry out attributes and methods
- Creating a score object from the 'Scoreboard' class to carry out attributes and methods
"""

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

""" Controls user input and it's display on screen """

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collisi
    # on with wall
    if ball.ycor() > 278 or ball.ycor() < -278:  # If the ball hits the top of the wall, it will switch the direction
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

"""
- Create a while loop 
- With move_speed set to 0.1, the game updates every 0.1 seconds, making the ball move at a steady pace. If move_speed 
is decreased, the game updates more frequently, speeding up the ball. If increased, the updates are less frequent, 
slowing the ball down.
- This smoothens the animation by reducing flicker, as the screen only updates when screen.update() is called, 
showing the latest state of the game elements.
- First if statement detects if the ball hits the top or bottom of the screen, if so it will bounce in the opposite 
direction.
- The second if statement detects if the ball has made contact with the paddle; So if the ball is within 50 units of 
distance from the paddle and if the ball hasn't hit the wall, then we will change the direction of the ball to bounce
the opposite way, as well as increase the speed (as the game keeps getting played, the speed will gradually increase)
- The last two if statements detect if the ball has made contact with the left or right wall. If so, the adjacent player
will gain a point and the ball will reset to the (0,0) position. 


"""