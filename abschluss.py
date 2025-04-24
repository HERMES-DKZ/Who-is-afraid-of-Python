import turtle
import time

# Fenster vorbereiten
screen = turtle.Screen()
screen.bgcolor("white")

# Zeichen-Turtle für Strichmännchen vorbereiten
zeichner = turtle.Turtle()
zeichner.hideturtle()
zeichner.speed(0)

# Text-Turtle vorbereiten
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)

# Funktion: Strichmännchen zeichnen
def strichmaennchen(t, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    # Kopf
    t.circle(10)

    # Körper
    t.right(90)
    t.forward(30)

    # Arme
    t.backward(15)
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(90)
    t.forward(15)
    t.backward(15)
    t.left(45)

    # Beine
    t.forward(15)
    t.left(30)
    t.forward(15)
    t.backward(15)
    t.right(60)
    t.forward(15)
    t.backward(15)
    t.left(30)

# Funktion: Figur neu zeichnen bei Bewegung
def bewege_strichmaennchen(start_x, end_x, y, schritte=30):
    walker = turtle.Turtle()
    walker.hideturtle()
    walker.speed(0)

    dx = (end_x - start_x) / schritte

    for i in range(schritte + 1):
        walker.clear()
        strichmaennchen(walker, start_x + i * dx, y)

# Rechtes Strichmännchen steht fest
strichmaennchen(zeichner, 100, 0)

# Linkes läuft hin
bewege_strichmaennchen(-150, 40, 0)

# Text anzeigen (erste Nachricht)
text_turtle.penup()
text_turtle.goto(-100, 100)
text_turtle.color("blue")
text_turtle.write("Siehst du, so schlimm ist Python gar nicht!", font=("Arial", 14, "bold"))

time.sleep(0.5)

# Ersten Text löschen
text_turtle.clear()

# Zweite Antwort (mit neuer Textanzeige)
text_turtle.penup()
text_turtle.goto(-100, 100)  # Neue Position für den zweiten Text
text_turtle.pendown()
text_turtle.color("red")
text_turtle.write("Stimmt! Danke für deine Hilfe\nBei weiteren Fragen wende ich mich einfach an das\nDatenkompetenzzentrum HERMES", font=("Arial", 14, "bold"))

turtle.done()
