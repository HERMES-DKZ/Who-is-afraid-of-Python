import turtle
import random
import time

# Fenster vorbereiten
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=300, height=300)

# Spieler (kleiner Kreis)
player = turtle.Turtle()
player.shape("circle")
player.color("blue")
player.penup()
player.goto(0, 0)
player.speed(0)

# Funktionsweise des Spielers
player_speed = 2

# Liste der Hindernisse (größere Kreise)
obstacles = []

# Funktion, die ein Hindernis erstellt
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    obstacle.color("red")
    obstacle.penup()
    x = random.randint(-140, 140)
    y = random.randint(-140, 140)
    obstacle.goto(x, y)
    obstacle.shapesize(stretch_wid=2, stretch_len=2)  # Größere Kreise
    obstacles.append(obstacle)

# Funktion, um den Spieler zu bewegen
def move_player():
    global player_speed
    player.setx(player.xcor() + player_speed)
    # Wenn der Spieler den Rand erreicht, kehre um
    if player.xcor() > 140 or player.xcor() < -140:
        player_speed *= -1  # Kehrt die Bewegungsrichtung um

    # Geschwindigkeit des Spielers erhöhen
    player_speed *= 1.01  # Wird jedes Mal ein bisschen schneller
    screen.ontimer(move_player, 20)  # Wiederhole die Bewegung alle 20ms

# Funktion, um Hindernisse zu entfernen
def remove_obstacles():
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:  # Kollision prüfen
            print("Kollidiert!")
            obstacle.hideturtle()
            obstacles.remove(obstacle)
    screen.ontimer(remove_obstacles, 100)  # Alle 100ms prüfen

# Funktion, die Hindernisse erzeugt
def generate_obstacles():
    create_obstacle()
    screen.ontimer(generate_obstacles, 4000)  # Alle 4 Sekunden ein neues Hindernis

# Starte das Spiel
screen.ontimer(move_player, 20)
screen.ontimer(generate_obstacles, 4000)
screen.ontimer(remove_obstacles, 100)

# Spiel starten
turtle.done()
