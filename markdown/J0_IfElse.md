# Fälle unterscheiden - bedingte Anweisungen

Bisher hatten wir nur Skripts, welche eine Abfolge von Anweisungen ausführen.
Manchmal möchtest du aber, dass dein Skript je nach 
Situation unterschiedliche Anweisungen ausführt.
Das kannst du mit bedingten Anweisungen erreichen.

Die einfachste Form einer bedingten Anweisung ist die `if`-Anweisung.
Sie hat die folgende Struktur:

```python
if Bedingung:
    Anweisung1
    Anweisung2
    ...
```

Die `Bedingung` ist ein Ausdruck, der entweder wahr oder falsch ist.
Wenn die `Bedingung` wahr ist, werden die `Anweisungen` ausgeführt.
Wenn die `Bedingung` falsch ist, werden die `Anweisungen` übersprungen.

Hier ist ein Beispiel:

```python
zahl = 5
if zahl > 0:
    print("Die Zahl ist positiv.")
```









[<<](I0_EinAusgabe.md) &emsp; [>>](K0_Schleifen.md)