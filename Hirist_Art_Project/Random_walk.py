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

# colors = rgb_color()
direction=[0,90,180,270,]
tim.speed("fastest")
def draw_line(n):
    tim.pensize(10)
    for i in range(n):
        tim.color(rgb_color())
        tim.forward(50)
        tim.setheading(random.choice(direction))
draw_line(300)