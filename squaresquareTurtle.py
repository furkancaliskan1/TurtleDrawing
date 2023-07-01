import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Easy")

a = turtle.Turtle()
a.color("white")

def square(size):
    for i in range(4):
        a.forward(size)
        a.left(90)

for x in range(50,300,50):
    square(x)
turtle.done()


