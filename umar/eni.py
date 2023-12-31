import turtle

def draw_shape():
    turtle.speed(0)
    turtle.pensize(1)
    turtle.color("black")
    for i in range(100):
        turtle.forward(i * 2)
        turtle.right(98)
    turtle.done()

draw_shape()
