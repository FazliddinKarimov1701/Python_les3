import turtle
t = turtle.Turtle()
t.pensize(5)
t.pencolor("blue")
t.fillcolor("dodgerblue")
t.circle(100)
for side in range(2000):
    t.forward(1)
    if t.xcor() < -200 or t.xcor() > 200:
        t.right(180)