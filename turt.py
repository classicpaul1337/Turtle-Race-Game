from turtle import Turtle


class Classic(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.goto(0, -380)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -380)
