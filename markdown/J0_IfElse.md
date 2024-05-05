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










[<<](I0_EinAusgabe.md) &emsp; [>>](K0_Schleifen.md)