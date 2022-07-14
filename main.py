import turtle
import paddle
import ball
import time
import scoreboard

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

scoreboard = scoreboard.ScoreBoard()
ball = ball.Ball((0, 0))
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    elif ball.distance(r_paddle) < 50 and ball.xcor() >= 340 or ball.distance(l_paddle) < 50 and ball.xcor() <= -340:
        ball.bounce_x()
    elif ball.xcor() > 360:
        ball.setposition(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        ball.move()
        scoreboard.add_score(scoreboard.lscore)
    elif ball.xcor() < -360:
        ball.setposition(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        ball.move()
        scoreboard.add_score(scoreboard.rscore)
    elif scoreboard.lscore == 5 or scoreboard.rscore == 5:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
