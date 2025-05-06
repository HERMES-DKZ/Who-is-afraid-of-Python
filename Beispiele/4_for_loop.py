import turtle

# Malen der Flagge aus Beispiel 1, nur dass zusätzlich eine for-Schleife verwendet wird, um den Code kürzer zu gestalten.

t = turtle.Turtle()
t.speed(3)

farben = ["black", "red", "gold"]


x = 0
y = 0

for farbe in farben:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.fillcolor(farbe)
    t.begin_fill()
    t.forward(300)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.end_fill()
    y = y - 80
    # Nach unten zum nächsten Balken

t.hideturtle()
turtle.done()
