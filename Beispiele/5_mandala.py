import turtle

# Malen eines Mandalas mit Hilfe einer Schleife

t = turtle.Turtle()
t.speed(0)

for i in range(36):
    t.circle(100)
    t.right(10)


turtle.done()