import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
game_is_on = True

screen.listen()
screen.onkey(player.move, "w")
while game_is_on:
    car = CarManager()
    time.sleep(0.1)
    car.carmove()
    screen.update()

