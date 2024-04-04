# Ergebnisse zwischenspeichern - Variablen

Es ist zwar schön, dass wir in der Python-Konsole Rechnungen durchführen können, aber meistens wollen wir die Ergebnisse speichern, um sie später wieder zu verwenden. Dazu verwenden wir Variablen. 
Eine Variable ist ein Behälter, in dem wir Werte speichern können.

Wenn du z.B. das Ergebnis der Berechnung der Fläche eines Rechtecks speichern möchtest, kannst du das so machen:

```python
>>> f = 3.5 * 4.7
```

In der Entwicklungsumgebung Thonny gibt es ein Fenster, in dem du die Werte von Variablen sehen kannst:

![img.png](../img/VariablenFenster.png)

Falls dieses Fenster bei dir nicht sichtbar ist, 
kannst du es über das Menu `Ansicht` -> `Variablen` einblenden.

Du kannst hier sehen, dass die Variable den Namen `f` und den Wert `4.7`hat.

## Variablennamen

Variablennamen dürfen nur aus Buchstaben, Zahlen und Unterstrichen bestehen.
Der Name darf nicht mit einer Zahl beginnen.
Groß- und Kleinschreibung wird unterschieden:

```python
>>> a = 3
>>> A = 4
```

![img.png](../img/Variablenfenster2.png)

Du solltest Variablennamen so wählen, dass sie aussagekräftig sind. 
Im oben gezeigten Beispiel ist `f` nicht sehr aussagekräftig.
Besser wäre z.B. `flaeche`:

```python
>>> flaeche = 3.5 * 4.7
```

Das gute an Variablen ist, dass du sie später wieder verwenden kannst:

```python
>>> doppelteFlaeche = 2 * flaeche
>>> doppelteFlaeche
32.9
```

Wie du in diesem Beispiel siehst, kannst du den Wert einer Variable auch anzeigen lassen, indem du einfach den Variablennamen eingibst.

