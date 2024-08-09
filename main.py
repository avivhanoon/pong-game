from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
scoreboard = ScoreBoard()
paddle1 = Paddle(x=350, y=0)
paddle2 = Paddle(x=-350, y=0)
ball = Ball()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or \
       (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        # Add some logic to keep track of score or end the game here if needed

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        # Add some logic to keep track of score or end the game here if needed

screen.exitonclick()
