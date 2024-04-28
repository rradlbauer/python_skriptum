# Debugger

Bald wirst du auch kompliziertere Scripts schreiben, bei denen du nicht mehr so einfach erkennen kannst, 
ob sie richtig funktionieren oder warum sie nicht richtig funktionieren.
Dann ist es hilfreich, wenn du den Debugger benutzt.
Der Debugger ist ein Werkzeug, mit dem du ein Script Schritt für Schritt durchgehen kannst,
um zu sehen, was bei jedem Schritt passiert.

In Thonny kannst du den Debugger starten, indem du auf das kleine Käfer-Symbol ![img.png](../img/start_debugging.png) klickst.
Dann wird das Script gestartet und bei jeder Anweisung angehalten.
Du kannst dann die Variablenwerte sehen und das Script Schritt für Schritt durchgehen.
Mit diesem Pfeil ![img_1.png](../img/debugging_step.png) gehst du einen Schritt weiter.
Mit Stop ![img_2.png](../img/stop_debugging.png) kannst du das Debugging beenden.
Mit dem grünen Pfeil ![img_3.png](../img/continue_debugging.png) kannst du das Script weiter laufen lassen. 
Es läuft dann bis zum nächsten Breakpoint oder bis zum Ende.

![img_4.png](../img/Breakpoint.png)

Einen Breakpoint setzt du, indem du in der Zeile, bei der du anhalten möchtest, auf die linke Seite klickst.

## Übung


- Gehe 3 deiner Scripts aus dem vorigen Abschnitt mit dem Debugger Schritt für Schritt durch.
Erstelle dabei eine Tabelle, in welcher du nach jeder Zeile des Scripts die Variablenwerte notierst.
Beispiel:

![img.png](../img/debugging_variablen.png) 


| Zeile | a   | b   | c   | s   | flaeche |
|-------|-----|-----|-----|-----|---------|
| 2     | 3   |     |     |     |         |
| 3     | 3   | 4   |     |     |         |
| 4     | 3   | 4   | 5   |     |         |
| 5     | 3   | 4   | 5   | 6.0 |         |
| 6     | 3   | 4   | 5   | 6.0 | 6.0     |
| 7     | 3   | 4   | 5   | 6.0 | 6.0     |



[<<](E0_Script.md) &emsp; [>>](G0_Funktionen.md)