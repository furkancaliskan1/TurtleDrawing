import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtleeeeeeeeeeeeeee")
a = turtle.Turtle()
a.color("white")
a.speed(0)
colors = ["orange","green","blue","red","yellow","white","pink"]
for i in range(15):
    a.color(colors[i % 7])
    a.circle(10*i)
    a.circle(-10*i)
    a.left(i)
turtle.done()