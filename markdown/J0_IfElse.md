# Fälle unterscheiden - bedingte Anweisungen

Bisher hatten wir nur Skripts oder Funktionen, 
welche eine Abfolge von Anweisungen ausführen.
Manchmal möchtest du aber, dass dein Skript je nach 
Situation unterschiedliche Anweisungen ausführt.
Das kannst du mit bedingten Anweisungen erreichen.

Die einfachste Form einer bedingten Anweisung ist die `if`-Anweisung.
Beispiel:

```python
eingabe = input("bitte Zahl eingeben:")
zahl = int(eingabe)
if zahl < 0:
    print(zahl, "ist negativ")
    zahl = -zahl
print("Betrag der eingegebenen Zahl:", zahl)
```

Hier wird zuerst vom Benutzer die Eingabe einer Zahl angefordert.
Du erinnerst dich sicher, dass die Funktion `input()` immer eine Zeichenkette zurückgibt.
Deshalb wird die Eingabe mit der Funktion `int()` in eine Ganzzahl umgewandelt.

Dann wird geprüft, ob die eingegebene Zahl negativ ist (`zahl < 0`).
Wenn das der Fall ist, wird die Information ausgegeben, dass die Zahl negativ ist.
Anschließend wird die Zahl positiv gemacht, indem das Vorzeichen umgedreht wird.

Zum Schluss wird der Betrag der eingegebenen Zahl ausgegeben.

Die `if`-Anweisung hat die allgemeine Form:

```python
if Bedingung:
    Anweisung1
    Anweisung2
    ...
weitere Anweisungen, welche immer ausgeführt werden
```

Als Bedingung kann alles verwendet werden, 
was einem Wahrheitswert (`bool`) entspricht
(erinnere dich an den Datentyp `bool` aus
dem Abschnitt [Datentypen](D1_Datentypen.md)).

Die Anweisungen, welche nach der Bedingung folgen und eingerückt sind,
werden nur ausgeführt, wenn die Bedingung wahr ist.

Die Anweisungen, welche nach der `if`-Anweisung folgen und nicht mehr eingerückt sind,
werden immer ausgeführt.

## else-Anweisung

Manchmal möchtest du auch Anweisungen ausführen, wenn die Bedingung nicht wahr ist.
Das kannst du mit der `else`-Anweisung erreichen.

Beispiel:

```python
eingabe = input("bitte Zahl eingeben:")
zahl = int(eingabe)
if zahl < 0:
    print(zahl, "ist negativ")
    zahl = -zahl
else:
    print(zahl, "ist positiv oder Null")
print("Betrag der eingegebenen Zahl:", zahl)
```

Hier wird die Eingabe wieder in eine Ganzzahl umgewandelt.
Dann wird geprüft, ob die eingegebene Zahl negativ ist.
Wenn das der Fall ist, wird die Information ausgegeben, dass die Zahl negativ ist.
Anschließend wird die Zahl positiv gemacht, indem das Vorzeichen umgedreht wird.

Wenn die Zahl nicht negativ ist, wird die Information ausgegeben, 
dass die Zahl positiv oder Null ist.

Zum Schluss wird der Betrag der eingegebenen Zahl ausgegeben. 
Diese Anweisung wird in jedem Fall ausgeführt.

Die `else`-Anweisung hat die allgemeine Form:

```python
if Bedingung:
    Anweisung1
    Anweisung2
    ...
else:
    Anweisung3
    Anweisung4
    ...
weitere Anweisungen, welche immer ausgeführt werden
```

## elif-Anweisung

Manchmal möchtest du mehrere Bedingungen prüfen.
Das kannst du mit der `elif`-Anweisung erreichen.

Beispiel:

```python
eingabe = input("bitte Körpertemperatur eingeben:")
temperatur = float(eingabe)
if temperatur < 36.0:
    print("Unterkühlung")
elif temperatur < 37.5:
    print("Normaltemperatur")
elif temperatur < 38.0:
    print("erhöhte Temperatur")
else:
    print("Fieber")
``` 

Hier wird die Eingabe wieder in eine Gleitkommazahl umgewandelt.
Dann wird geprüft, ob die eingegebene Temperatur unter 36.0 ist.
Wenn das der Fall ist, wird die Information ausgegeben, dass eine Unterkühlung vorliegt.

Wenn die Temperatur nicht unter 36.0 ist, wird geprüft, ob sie unter 37.5 ist.
Wenn das der Fall ist, wird die Information ausgegeben, dass die Temperatur normal ist.

Wenn die Temperatur nicht unter 37.5 ist, wird geprüft, ob sie unter 38.0 ist.
Wenn das der Fall ist, wird die Information ausgegeben, dass die Temperatur erhöht ist.

Wenn die Temperatur nicht unter 38.0 ist, wird die Information ausgegeben, dass Fieber vorliegt.


Die `elif`-Anweisung hat die allgemeine Form:

```python
if Bedingung1:
    Anweisung1
    Anweisung2
    ...
elif Bedingung2:
    Anweisung3
    Anweisung4
    ...
elif Bedingung3:
    Anweisung5
    Anweisung6
    ...
else:
    Anweisung7
    Anweisung8
    ...
weitere Anweisungen, welche immer ausgeführt werden
```


## [Übungen](../uebungen/UE_J0_IfElse.md)








[<<](I0_EinAusgabe.md) &emsp; [>>](K0_Listen.md)