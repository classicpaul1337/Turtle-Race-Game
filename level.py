from turtle import Turtle
FONT = ('Courier', 24, 'normal')
with open('level.txt') as level:
    LEVEL = int(level.read())


# Create a LevelBoard Class and inherit the Turtle Class
class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move = 5
        self.lives = 3
        self.level = 1
        self.highest_level = LEVEL
        self.timer = 0.1
        self.penup()
        self.update_board()

# Update board function
    def update_board(self):
        self.goto(-380, 360)
        self.write(f'Level: {self.level}', move=False, align='left', font=FONT)
        self.goto(250, 360)
        self.write(f'Lives: {self.lives}', move=False, align='left', font=FONT)
        self.goto(-110, 360)
        self.write(f'Highest Level: {self.highest_level}', move=False, align='left', font=FONT)

# Increase level and move speed when the turtle reached the finish line.
    def check_score(self):
        self.clear()
        self.level += 1
        self.move += 1
        self.update_board()

# Display Game Over when the turtle lives goes to Zero
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Courier', 30, 'normal'))

# Decrease life when the turtle collide with a car
    def live(self):
        self.clear()
        self.lives -= 1
        self.update_board()

# Check for high score then update board
    def high_level(self):
        if self.level > self.highest_level:
            with open('level.txt', mode='w') as update_level:
                update_level.write(str(self.level))
                self.highest_level = self.level
            self.clear()
            self.update_board()
