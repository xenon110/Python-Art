from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()
screen.title("Xenon Turtle")
screen.bgcolor("pink")
tim.pensize(3)
tim.begin_fill()
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
def change_corol():
    tim.color(random.choice(colors))
def move_back():
    change_corol()
    tim.setheading(270)
    tim.forward(20)
    tim.end_fill()
def move_forward():
    change_corol()
    tim.setheading(90)
    tim.forward(20)
    tim.end_fill()
def move_right():
    change_corol()
    tim.setheading(0)
    tim.forward(20)
    tim.end_fill()
def move_left():
    change_corol()
    tim.setheading(180)
    tim.forward(20)
    tim.end_fill()
def arc_left():
    change_corol()
    tim.circle(50, 90)  # 50 is the radius, 90 is the extent of the arc
    tim.end_fill()
def arc_right():
    change_corol()
    tim.circle(-50, 90)
    tim.end_fill()
def fill_shape():
    change_corol()
    tim.end_fill()

screen.listen()
screen.onkey(key="s",fun=move_back)
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="t",fun=arc_right)
screen.onkey(key="r",fun=arc_left)
screen.onkey(key="f", fun=fill_shape)
screen.exitonclick()
#
# class Car:
#
#     def __init__(self):
#         self.wheel=4
#         self.body="hard"
#
#     def function(self):
#         print("It have 400cc engine")
#
# class Car_collection(Car):
#
#     def __init__(self):
#         super().__init__()
#         self.body="not hard"
#     def Maruti(self):
#         print("maruti is fantastics veichle")
#
#     def Landrover(self):
#         print("landrover is very heavy and roaring car")
#
#
# #
# # collection=Car_collection()
# # collection.body()
# # collection.Landrover()
# collection.function()
#
#
#
#
#







