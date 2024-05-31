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
speed(10)
color('red')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('blue')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('yellow')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('green')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('red')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('blue')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('yellow')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('green')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
left(20)
color('blue')
begin_fill()
begin_fill()
forward(200)
left(95)
forward(35)
left(95)
forward(400)
right(95)
forward(35)
right(95)
forward(200)
end_fill()
```

Zugegeben - die Zeichnung ist kein Meisterwerk. Wahrscheinlich kannst du es besser.
Aber das Beispiel zeigt dir, wie du mit der Schildkröte zeichnen kannst.

Im Internet gibt es viele Tutorials für das Modul `turtle`.
Hier ist eines davon:

[Turtle-Modul von Python](https://www.python-lernen.de/python-turtle.htm) 
*(in diesem Tutorial wird das Modul anders importiert,
so dass vor jedem Funktionsaufruf der Modulname `turtle` 
geschrieben werden muss.)*

[<<](H0_Module.md) &emsp; [>>](I0_EinAusgabe.md)