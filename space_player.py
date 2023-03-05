from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    '''creates the playerturtle at a fixed starting position (STARTING_POSITION)'''
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(180)
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.move_left()
        self.move_left()

        self.bullets = []
        self.shoot()

    def move_right(self):
        '''Turns the turtle right on its own axis.'''
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        '''Turns the turtle left on its own axis.'''
        self.forward(MOVE_DISTANCE)

    def shoot(self):
        new_shot = True
        return new_shot

    def bullet(self, player_xcor, player_ycor):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("circle")
        bullet.color("white")
        bullet.shapesize(0.3)
        bullet.goto(player_xcor, player_ycor)
        bullet.setheading(90)
        self.bullets.append(bullet)
        self.shape()

    def shoot_dem(self):
        self.bullet(player_xcor=self.xcor(), player_ycor=self.ycor())
        self.bullet_move()

    def bullet_move(self):
        for bul in self.bullets:
            bul.setheading(90)
            bul.forward(40)
