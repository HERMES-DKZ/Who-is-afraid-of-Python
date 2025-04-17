# 🐢 Python Turtle Cheat Sheet

## 📦 Setup

```python
import turtle          # Turtle-Modul laden
t = turtle.Turtle()    # Eine Turtle-Instanz erzeugen
```

---

## 🧭 Bewegung

| Funktion                | Beschreibung                                           |
|-------------------------|--------------------------------------------------------|
| `t.forward(x)`          | Bewegt die Turtle `x` Pixel vorwärts.                 |
| `t.backward(x)`         | Bewegt die Turtle `x` Pixel rückwärts.                |
| `t.left(angle)`         | Dreht die Turtle um `angle` Grad nach links.          |
| `t.right(angle)`        | Dreht die Turtle um `angle` Grad nach rechts.         |
| `t.goto(x, y)`          | Springt zu Koordinaten `(x, y)`.                      |
| `t.setheading(angle)`   | Setzt die Blickrichtung der Turtle (0 = rechts).      |
| `t.home()`              | Zurück zur Startposition und Richtung.                |
| `t.circle(radius)`      | Zeichnet einen Kreis mit gegebenem Radius.            |
| `t.speed(n)`            | Setzt Zeichen-Geschwindigkeit (0 = sofort, 1–10).     |

---

## 🖍️ Zeichnen

| Funktion                 | Beschreibung                                           |
|--------------------------|--------------------------------------------------------|
| `t.pendown()`            | Stift senken – ab jetzt wird gezeichnet.              |
| `t.penup()`              | Stift heben – Bewegung ohne Zeichnen.                 |
| `t.pensize(n)`           | Setzt die Stiftbreite auf `n`.                        |
| `t.color("red")`         | Setzt die Stiftfarbe.                                 |
| `t.fillcolor("blue")`    | Setzt die Füllfarbe.                                  |
| `t.begin_fill()`         | Beginnt eine Füllung.                                 |
| `t.end_fill()`           | Beendet die Füllung mit aktueller Farbe.              |
| `t.clear()`              | Löscht die Zeichenfläche.                             |
| `t.reset()`              | Setzt Turtle zurück (Position, Farbe, Richtung).      |

---



## 🧠 Nützliches

| Funktion                      | Beschreibung                                           |
|-------------------------------|--------------------------------------------------------|
| `turtle.done()`               | Beendet das Programm – hält das Fenster offen.         |
| `turtle.bgcolor("color")`     | Setzt die Hintergrundfarbe der Zeichenfläche.         |
| `t.hideturtle()`              | Versteckt die Turtle.                                 |
| `t.showturtle()`              | Zeigt die Turtle wieder an.                           |




---

## 🖥️ Fenstersteuerung und Interaktivität (optional)

```python
screen = turtle.Screen()
```

| Funktion                      | Beschreibung                                           |
|-------------------------------|--------------------------------------------------------|
| `screen.bgcolor("black")`               | Hintergrundfarbe ändern.                     |
| `screen.title("Mein Fenster")`     | Fenstertitel setzen.                              |
| `screen.setup(600, 400)`              | Fenstergröße (Breite, Höhe).                   |
| `screen.mainloop()`              | Startet das Hauptloop (nur bei Skripten nötig).     |
| `screen.listen()`     | Warten auf Tastatureingabe.                                    |
| `screen.onkey(func, "Taste")`              | Verknüpft eine Taste mit einer Funktion.  |
| `screen.ontimer(func, ms)`              | Führt Funktion nach `ms` Millisekunden aus.  |


---

