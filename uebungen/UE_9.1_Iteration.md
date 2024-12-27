# UE_9.1 Iteration - Übungen

### UE_9.1_1: Summe der Zahlen in einer Liste

Schreibe Funktion, welcher als Parameter eine Liste von Zahlen übergeben wird. 
Die Funktion gibt dann die Summe der Zahlen in der Liste zurück.

    Anleitung: Definiere in der Funktion eine Variable `summe` mit dem Wert 0.
    Gehe dann alle Elemente der Liste durch und addiere sie zur `summe`.
    Gib am Ende die `summe` zurück.

### UE_9.1_2: Quadratzahlen

Schreibe eine Funktion, 
welcher als Parameter eine Liste von Zahlen übergeben wird.
Die Funktion gibt eine Liste zurück, 
welche die Quadrate der Zahlen der übergebenen Liste enthält.

    Anleitung: Definiere in der Funktion eine leere Liste `quadrate`.
    Gehe dann alle Elemente der übergebenen Liste durch und füge das Quadrat des Elements
    der Liste `quadrate` hinzu.
    Gib am Ende die Liste `quadrate` zurück.

### UE_9.1_3: Labyrinth

![TurtleGrafikLabyrinth.png](../img/9.1/TurtleGrafikLabyrinth.png)

Dieses Bild wurde mit [turtle](../skriptum/6.0_turtle.md) erstellt.
In einer Schleife wurde immer wieder `forward(...)` 
und anschließend `left(90)` aufgerufen.
Der Wert für `forward` wurde in jedem Schritt um 2 erhöht.

Schreibe eine Funktion, welche ein Labyrinth zeichnet.
Die Funktion soll einen Parameter `n` haben,
welcher die Anzahl der Aufrufe von `forward(...)` angibt.

[<<](../skriptum/9.1_Iteration.md)