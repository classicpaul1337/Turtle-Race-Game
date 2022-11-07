from turtle import Screen
from turt import Classic
from level import LevelBoard
from motor import Motor
import time
import random

screen = Screen()
screen.setup(width=800, height=800)
screen.title('Classic Race Game')
screen.tracer(0)
level = LevelBoard()
classic = Classic()
motor = Motor()
screen.listen()
screen.onkey(classic.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(level.timer)
# Keep all cars moving, reset the car if it has gone pass the x-axis, also check for collide with the turtle
    for i in range(motor.cars):
        motor.motor[i].back(level.move)
        if motor.motor[i].xcor() < -420:
            motor.motor[i].goto(random.randint(400, motor.limit), random.randint(-360, 350))
        if classic.distance(motor.motor[i]) <= 20:
            level.live()
            classic.reset()
# Check if the turtle has reached the finish line, then reset to starting point and increase level
    if classic.ycor() >= 390:
        classic.reset()
        level.check_score()
# Check if the turtle lives has gone to zero, then stop the game
    if level.lives == 0:
        level.high_level()
        level.game_over()
        game_is_on = False


screen.exitonclick()
