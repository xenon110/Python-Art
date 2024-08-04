from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        supper().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=10,stretch_wid=10)
        self.color("blue")
        self.speed("fastest")
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)