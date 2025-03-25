from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong')
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  #Detecting the collision with ball

  if ball.ycor()>280 or ball.ycor()<-280:
    ball.bounce()

  # Detecting the collision with  right paddle

  if ball.xcor()>325 or ball.xcor() < -325:
    if ball.distance(l_paddle)<50 or ball.distance(r_paddle)<50:
      ball.collide()
    elif ball.xcor()>355 or ball.xcor() < -355:
      ball.reset_position()


screen.exitonclick()