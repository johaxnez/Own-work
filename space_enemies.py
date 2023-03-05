import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Enemies:

    def __init__(self):
        self.all_enemies = []

    def create_enemy(self):
        random_chance = random.randint(1, 40)
        if random_chance == 1:
            new_enemy = Turtle("square")
            new_enemy.shapesize(stretch_len=2, stretch_wid=1)
            new_enemy.penup()
            new_enemy.color(COLORS[random.randint(0, 5)])
            random_x = random.randint(-250, 250)
            new_enemy.goto(random_x, 300)
            self.all_enemies.append(new_enemy)

    def move_enemy(self):
        for enemy in self.all_enemies:
            enemy.setheading(270)
            enemy.forward(STARTING_MOVE_DISTANCE)
            enemy.position()

