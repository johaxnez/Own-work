import time
from turtle import Screen
from space_enemies import Enemies
from space_scoreboard import Scoreboard

from space_player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
time_sleep = 0.1

player = Player()
enemies = Enemies()
space_scoreboard = Scoreboard()


player_xcor = player.xcor()

screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

screen.onkeypress(player.shoot_dem, "space")

game_is_on = True

while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    enemies.create_enemy()
    enemies.move_enemy()
    screen.update()
    for bul in player.bullets:
        bul.forward(20)

    for enemy in enemies.all_enemies:
        for bullet in player.bullets:
            if enemy.distance(bullet) < 20:
                enemy.hideturtle()
                enemies.all_enemies.remove(enemy)
                space_scoreboard.point()

    for enemy in enemies.all_enemies:
        if enemy.ycor() < -230 > -236:
            enemy.hideturtle()
            enemies.all_enemies.remove(enemy)
            space_scoreboard.life_lost()

    if space_scoreboard.lives == 0:
        game_is_on = False

    screen.update()

space_scoreboard.goto(0, 0)
space_scoreboard.write("GAME OVER", align="center", font=("Courier", 50, "normal"))


screen.exitonclick()