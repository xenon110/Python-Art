import turtle as t
tim = t.Turtle()
import random

t.colormode(255)
def rgb_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return random_color

tim.setheading(230)
tim.hideturtle()
tim.penup()
tim.forward(300)
tim.setheading(0)
no_of_dots=101
tim.speed("fastest")


for dot_count in range(1,no_of_dots):
    tim.dot(20,rgb_color())
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=t.Screen()
screen.exitonclick()