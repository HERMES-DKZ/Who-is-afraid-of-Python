import turtle

# Malen von Länderflaggen

t = turtle.Turtle()


# Schwarzer Balken
t.fillcolor("black")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(80)
t.left(90)
t.forward(300)
t.left(90)
t.forward(80)
t.end_fill()

# Roter Balken
t.fillcolor("red")
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(300)
t.left(90)
t.forward(80)
t.end_fill()

# Goldener Balken
t.penup()
t.left(180)
t.forward(80)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.forward(80)
t.right(90)
t.forward(300)
t.right(90)
t.forward(80)
t.end_fill()





turtle.done()