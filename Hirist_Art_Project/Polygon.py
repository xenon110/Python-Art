import turtle as t
tim=t.Turtle()
colors = ["red", "blue", "green"]
def draw_shape(n):
    tim.pensize(2)
    for i in range(n):
        angle = 360 / n
        tim.color(colors[i%len(colors)])
        tim.forward(100)
        tim.right(angle)
for draw_sides in range(3,11):
    draw_shape(draw_sides)
