import turtle
t = turtle.Turtle()
# t.begin_fill()
t.color("pink")
# t.pensize(5)
# t.circle(100)
# t.end_fill()
# for side in range(800):
#     t.forward(1)
#     if t.xcor() < -200 or t.xcor() > 200:
#         t.right(180)
# t.clear()
# t.stamp()
# t.forward(300)
# t.clearstamp(1)
# t.right(180)
# t.forward(600)
n=10
while n <= 40:
    t.goto(-200,-100)
    t.circle(n)
    n = n+10
