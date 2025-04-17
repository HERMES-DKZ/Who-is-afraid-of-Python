import turtle

# Bildschirm einrichten
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bewegender Kreis")

# Kreis erstellen
kreis = turtle.Turtle()
kreis.shape("circle")
kreis.color("blue")
kreis.penup()
kreis.goto(-200, 0)  # Startposition

# Funktion für die Bewegung
def bewege_kreis():
    while True:
        kreis.forward(2)  # Kreis bewegt sich nach vorne
        if kreis.xcor() > 300:  # Wenn der Kreis den Bildschirm verlässt
            kreis.goto(-300, 0)  # Setze den Kreis zurück zur Startposition

# Animation starten
bewege_kreis()

# Animation beenden
turtle.done()
