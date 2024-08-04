import turtle as t
tim=t.Turtle()
import random

t.colormode(255)
def rgb_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return random_color

def draw_spirograp(size):
    for _ in range(int(360/size)):
            tim.pensize(2)
            tim.speed("fastest")
            tim.circle(100)
            tim.setheading(tim.heading()+size)
            tim.color(rgb_color())

draw_spirograp(15)
screen=t.Screen()
screen.exitonclick()