import turtle

t = turtle.Turtle()
t.speed(3)

# Hauskörper (hellblaues Rechteck)
t.color("black", "lightblue")
t.penup()
t.goto(-100, -100)  # untere linke Ecke
t.pendown()
t.begin_fill()
t.goto(100, -100)   # untere rechte Ecke
t.goto(100, 100)    # obere rechte Ecke
t.goto(-100, 100)   # obere linke Ecke
t.goto(-100, -100)  # zurück zum Anfang
t.end_fill()

# Dach (braunes Dreieck)
t.color("black", "brown")
t.penup()
t.begin_fill()
t.goto(0, 180)      # Dachspitze
t.pendown()
t.goto(100, 100)    # obere rechte Ecke
t.goto(-100, 100)   # obere linke Ecke
t.goto(0, 180)      # zurück zur Spitze
t.end_fill()

# Tür (dunkelrote Rechtecktür)
t.penup()
t.color("black", "darkred")
t.goto(-30, -100)   # untere linke Ecke der Tür
t.pendown()
t.begin_fill()
t.goto(30, -100)    # untere rechte Ecke
t.goto(30, 0)       # obere rechte Ecke
t.goto(-30, 0)      # obere linke Ecke
t.goto(-30, -100)   # zurück zum Anfang
t.end_fill()

t.hideturtle()
turtle.done()
