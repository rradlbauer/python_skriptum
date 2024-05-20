# Eingabe und Ausgabe

Wir haben bisher zwei Arten von Python Skripten kennengelernt:
- Skripte, die etwas berechen und das Ergebnis ausgeben oder in Variablen speichern
- Skripte, die Funktionen definieren, 
die in anderen Skripten oder in der Python Konsole aufgerufen werden können.

Die erste Art von Skripten ist ein Computer-Programm im eigentlichen Sinne: 
Ein Programm, das eine Eingabe verarbeitet und eine Ausgabe erzeugt.

Allerdings haben wir bisher nur die Ausgabe auf der Konsole gesehen.
Zur Wiederholung: Auf die Konsole kann man mit der Funktion `print()` schreiben.

Ein ganz einfaches Computerprogramm ist das folgende Skript `hallo.py`:

```python
print("Hallo Welt!")
```

Wenn du das Skript mit nur dieser einen Zeile in Thonny ausführst,
wird "Hallo Welt!" auf der Konsole ausgegeben:

```python
>>> %Run hallo.py
Hallo Welt!
```

Mit der Funktion `input()` kannst du die Benutzer deines Programms 
eine Eingabe machen lassen:

```python
name = input("Wie heißt du? ")
print("Hallo", name)
```

Wenn du dieses Skript ausführst, wird zuerst die Frage "Wie heißt du?" auf der Konsole ausgegeben.
Dann kannst du deinen Namen eingeben und mit Enter bestätigen.
Danach wird "Hallo" und dein Name ausgegeben:

```python
>>> %Run hallo.py
Wie heißt du? Susanne
Hallo Susanne
```

Mit der Funktion `input()` wird immer eine Zeichenkette zurückgegeben.
Auch wenn du eine Zahl eingibst, wird sie als Zeichenkette zurückgegeben.
Du kannst das in der Kommandozeile ausprobieren:

```python
>>> eingabe = input("Wie alt bist du? ")
Wie alt bist du? 15
```

Die Variable `eingabe` enthält jetzt die Zeichenkette "15". 
Das kannst du im Variablenfenster sehen.


Mit einer Zeichenkette kannst du nicht rechnen.
Du kannst sie aber in eine Zahl umwandeln, 
indem du die Funktion `int()` oder `float()` verwendest:

```python
eingabe = input("Wie alt bist du? ")
alter = int(eingabe)
haelfte = alter/2
print('vor', haelfte ,'Jahren warst du halb so alt.')
```

Hier kannst du einen Ablauf dieses Programms sehen:

```python
>>> %Run hallo.py
Wie alt bist du? 14
vor 7.0 Jahren warst du halb so alt.
```

Als letzte Beispiel kommt jetzt ein Programm, 
welches die Fläche eines Dreiecks berechnet:

```python
def dreiecks_flaeche(a, b, c):
    s = (a + b + c) / 2
    flaeche = (s * (s - 3) * (s - 4) * (s - 5)) ** 0.5
    return flaeche

print('Dieses Programm berechnet die Fläche eines Dreiecks')
# Benutzer geben hier die Seitenlängen ein
str1 = input('Länge der 1. Seite: ')
str2 = input('Länge der 2. Seite: ')
str3 = input('Länge der 3. Seite: ')
# input() liefert den Datentyp str (Zeichenkette)
# diese muss erst in eine Zahl umgewandelt werden.
# das macht die Funktion float()
x = float(str1)
y = float(str2)
z = float(str3)
f = dreiecks_flaeche(x, y, z)
print('Fläche des Dreiecks: ', f)
```

In diesem Skript wird zuerst die Funktion `dreiecks_flaeche` definiert,
wie wir sie schon öfter gesehen haben.

Dann wird der Benutzer aufgefordert, die Seitenlängen des Dreiecks einzugeben.
Die Funktion `input()` gibt eine Zeichenkette zurück,
die mit `float()` in eine Zahl umgewandelt wird.

Die Funktion `dreiecks_flaeche` wird mit den eingegebenen Zahlen aufgerufen.
Das Ergebnis wird in der Variable `f` gespeichert und mit `print()` ausgegeben.

Hier ein Ablauf des Programms:

```python
>>> %Run allgemeines_dreieck.py
Dieses Programm berechnet die Fläche eines Dreiecks
Länge der 1. Seite: 3.2
Länge der 2. Seite: 3.9
Länge der 3. Seite: 4.3
Fläche des Dreiecks:  4.2794976340687425
```

## [Übungen](../uebungen/UE_I0_EinAusgabe.md)




[<<](H1_Turtle.md) &emsp; [>>](J0_IfElse.md)









