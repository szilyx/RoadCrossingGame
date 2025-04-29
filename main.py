import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
game_is_on = True
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move, "w")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.createcar()
    carmanager.carmove()

    for car in carmanager.car_storage:
        if car.distance(player) < 20:
            game_is_on = False
    if player.ycor() == 300:
        player.goto(0, -250)
        score_board.increase_score()
        carmanager.level_up()
screen.exitonclick()