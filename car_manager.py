from random import choice
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-280,280))

    def carmove(self):
        self.goto(self.xcor()-STARTING_MOVE_DISTANCE, self.ycor())


