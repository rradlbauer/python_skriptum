# Zeichnen mit der Schildkröte (Modul turtle)

Es gibt ein Modul in Python, das dir erlaubt, in einem eingenen Fenster zu zeichnen.
Das Modul heißt `turtle`. Importiere es mit folgender Anweisung:

```python
>>> import * from turtle
```

Im Variablenfenster kannst du nun alle Funktionen sehen, 
die du mit dem Modul `turtle` importiert hast.
Wenn du Hilfe zu einer Funktion benötigst, kannst du die Funktion `help` verwenden.
Beispiel:

```python
>>> help(forward)
```

Kopiere den folgenden Code in ein neues Skript und führe es aus:

```python
from turtle import *
penup()
backward(200)
pendown()
color('red')
begin_fill()
forward(400)
left(90)
forward(100)
left(90)
forward(50)
right(90)
forward(70)
right(90)
forward(20)
left(90)
forward(10)
left(90)
forward(65)
left(90)
forward(10)
left(90)
forward(20)
right(90)
forward(70)
right(90)
forward(150)
right(90)
forward(120)
left(90)
forward(175)
left(90)
forward(220)
end_fill()
color('black')
left(90)
penup()
forward(360)
pendown()
left(180)
begin_fill()
circle(30)
end_fill()
penup()
forward(80)
pendown()
begin_fill()
circle(30)
end_fill()
penup()
forward(80)
pendown()
begin_fill()
circle(30)
end_fill()
penup()
forward(80)
pendown()
begin_fill()
circle(30)
end_fill()
penup()
forward(80)
pendown()
begin_fill()
circle(30)
end_fill()
penup()
right(90)
forward(110)
color('blue')
pendown()
begin_fill()
forward(80)
right(90)
forward(100)
right(90)
forward(80)
right(90)
forward(100)
end_fill()
```

Zugegeben - die Zeichnung ist kein Meisterwerk. Wahrscheinlich kannst du es besser.
Aber das Beispiel zeigt dir, wie du mit der Schildkröte zeichnen kannst.

Im Internet gibt es viele Tutorials für das Modul `turtle`.
Hier ist eines davon:

[Turtle-Modul von Python](https://www.python-lernen.de/python-turtle.htm)

[<<](H0_Module.md) &emsp; [>>](I0_EinAusgabe.md)