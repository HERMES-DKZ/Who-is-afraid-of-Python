# Who-is-afraid-of-Python 🐢

Herzlich Willkommen zu diesem kleinen Coding-Sprint mit Python! 🎉

In diesem Workshop geht es darum, auf spielerische und kreative Weise mit der Programmiersprache Python in Berührung zu kommen – ganz unabhängig vom Erfahrungsstand. Ob du zum ersten Mal Python ausprobierst oder bereits regelmäßig damit arbeitest: Hier kannst du dich ausprobieren, experimentieren und gestalten.

Wir nutzen dafür die Standardbibliothek [**Turtle**](https://docs.python.org/3/library/turtle.html). Turtle eignet sich hervorragend zum Einstieg ins Programmieren, da sie visuelles Feedback gibt – man sieht direkt, was man programmiert hat. Gleichzeitig können Fortgeschrittene mit Turtle auch sehr komplexe grafische Strukturen oder sogar Animationen erzeugen. Um Python zu nutzen könnt ihr folgende [Onine-IDE](https://www.101computing.net/python/) verwenden oder eure lokale Instanz in einem Editor eurer Wahl. Um Python bei euch lokal zu installieren, findet ihr [hier](https://www.python.org/downloads/) die nötigen Dateien. Die Beispiele 6 und 7 sind leider nur auf einer lokalen Instanz möglich auszuführen.

## Ziel des Workshops

Die Aufgabe besteht darin, das HERMES-Logo mit Turtle grafisch umzusetzen – entweder möglichst originalgetreu oder als kreative Neuinterpretation. Dabei könnt ihr z.B.:

- das Logo Stück für Stück mit einfachen Formen "nachzeichnen",
- eine interaktive Animation bauen,
- mit Farben und Wiederholungen experimentieren,
- das Logo in Bewegung setzen,
- oder etwas ganz Eigenes erschaffen, das von der Idee des Logos inspiriert ist.

Eurer Kreativität sind keine Grenzen gesetzt! 🧠🎨

![HERMES-Logo](hermes_logo.png)

## Materialien im Repository

Dieses GitHub-Repo enthält alles, was ihr für den Workshop braucht:

📁 **Beispiele/** – kleine Python-Skripte, die zeigen, was mit Turtle möglich ist. Ideal zum Nachvollziehen und Modifizieren.  
📄 **turtle_cheat_sheet.md** – eine praktische Übersicht der wichtigsten Turtle-Befehle.  

## Wie funktioniert Turtle?

Turtle simuliert einen „Stift“, der sich über die Leinwand (den Bildschirm) bewegt und dabei Spuren hinterlässt. Diese Bewegung wird über Python-Befehle gesteuert – z.B. vorwärts, rückwärts, drehen, Stift heben, Farbe ändern usw.

Das Prinzip ist einfach:

```python
import turtle

t = turtle.Turtle()

t.forward(100)   # Geht 100 Schritte vorwärts
t.right(90)      # Dreht dich 90 Grad nach rechts
t.forward(100)   # Geht erneut 100 Schritte vorwärts
t.penup()        # Hebt den Stift
t.goto(0, 100)   # Bewegt sich zu Koordinate x = 0 , y = 100
t.pendown()      # Setzt Stift wieder ab
t.forward(80)    # Geht 80 Schritte vorwärts
turtle.done()    # Beendet das Malen und lässt das Fenster geöffnet
```
Mit den Funktionen in diesem Code würde sich bereits das HERMES-Logo und viele weitere Formen malen lassen. Es gibt allerdings noch viele weitere Möglichkeiten turtle zu nutzen. Werdet kreativ und probiert Dinge einfach aus. 
