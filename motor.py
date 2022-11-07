from turtle import Turtle
import random
COLORS = ['blue', 'green', 'yellow', 'purple', 'red', 'orange']


# Create a Motor Class
class Motor:
    def __init__(self):
        self.cars = 50
        self.limit = 3000
        self.motor = []
        for i in range(self.cars):
            self.create_cars()

# Function in charge of creating the cars.
    def create_cars(self):
        classic = Turtle()
        classic.shape('square')
        classic.penup()
        classic.color(random.choice(COLORS))
        classic.shapesize(stretch_len=2)
        classic.goto(random.randint(400, self.limit), random.randint(-360, 350))
        self.motor.append(classic)
