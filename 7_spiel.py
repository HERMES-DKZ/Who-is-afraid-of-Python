import turtle
import random

# Fenster vorbereiten
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=500, height=500)  # Größeres Spielfeld

# Spieler (kleiner Kreis)
player = turtle.Turtle()
player.shape("circle")
player.color("blue")
player.penup()
player.goto(0, 0)
player.speed(0)

# Funktionsweise des Spielers
player_speed = 2
max_speed = 5  # Maximale Geschwindigkeit

# Richtung des Spielers (global, damit sie in den Funktionen geändert werden kann)
player_direction = "right"

# Liste der Hindernisse (größere Kreise)
obstacles = []

# Funktion, die ein Hindernis erstellt
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    obstacle.color("red")
    obstacle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    obstacle.goto(x, y)
    obstacle.shapesize(stretch_wid=2, stretch_len=2)  # Größere Kreise
    obstacles.append(obstacle)

# Funktion, um die Richtung des Spielers zu ändern
def turn_left():
    global player_direction  # Hier wird player_direction als global definiert
    player_direction = "left"

def turn_right():
    global player_direction  # Hier wird player_direction als global definiert
    player_direction = "right"

def turn_up():
    global player_direction  # Hier wird player_direction als global definiert
    player_direction = "up"

def turn_down():
    global player_direction  # Hier wird player_direction als global definiert
    player_direction = "down"

# Funktion, die die Bewegung des Spielers steuert
def move_player():
    global player_speed, player_direction  # Beide Variablen müssen global gemacht werden

    if player_direction == "right":
        player.setx(player.xcor() + player_speed)
    elif player_direction == "left":
        player.setx(player.xcor() - player_speed)
    elif player_direction == "up":
        player.sety(player.ycor() + player_speed)
    elif player_direction == "down":
        player.sety(player.ycor() - player_speed)

    # Wenn der Spieler den Rand erreicht, kehrt er um
    if player.xcor() > 230 or player.xcor() < -230:
        player_direction = "left" if player_direction == "right" else "right"
    if player.ycor() > 230 or player.ycor() < -230:
        player_direction = "down" if player_direction == "up" else "up"

    # Bewege den Spieler alle 20 ms
    screen.ontimer(move_player, 20)

# Funktion, die die Geschwindigkeit des Spielers langsam erhöht
def increase_speed():
    global player_speed  # Hier wird player_speed als global definiert
    if player_speed < max_speed:
        player_speed *= 1.01  # Geschwindigkeit leicht erhöhen
    screen.ontimer(increase_speed, 100)  # Geschwindigkeit alle 100ms erhöhen

# Funktion, um Hindernisse zu entfernen
def remove_obstacles():
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:  # Kollision prüfen
            game_over()  # Wenn Kollision, Game Over
            return
    screen.ontimer(remove_obstacles, 100)  # Alle 100ms prüfen

# Funktion, die Hindernisse erzeugt
def generate_obstacles():
    create_obstacle()
    screen.ontimer(generate_obstacles, 4000)  # Alle 4 Sekunden ein neues Hindernis

# Funktion, die Game Over anzeigt
def game_over():
    player.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    obstacles.clear()

    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.color("red")
    game_over_text.write("Game Over", align="center", font=("Arial", 24, "bold"))

# Steuerung mit den Pfeiltasten
screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(turn_up, "Up")
screen.onkey(turn_down, "Down")

# Starte das Spiel
screen.ontimer(move_player, 20)  # Start der Bewegung des Spielers
screen.ontimer(increase_speed, 100)  # Geschwindigkeit langsam erhöhen
screen.ontimer(generate_obstacles, 4000)  # Alle 4 Sekunden ein neues Hindernis
screen.ontimer(remove_obstacles, 100)  # Kollisionen alle 100ms prüfen

# Spiel starten
turtle.done()
