# UE_5.0 Funktionen - Übungen

Bei diesen Übungen geht es darum, Funktionen zu schreiben.
Du kannst alle Funktionen in einem Skript schreiben oder in mehreren Skripten.
Die Funktionen sollen auf jeden Fall getestet werden.

Zur Qualitätssicherung muss bei jeder Funktion ein Kommentar
sein, der beschreibt, wie die Funktion getestet wurde.

In deinem Protokoll soll sich daher zu jeder Übung folgender Inhalt befinden
- der Programmcode der Funktion
- eine Beschreibung, wie die Funktion getestet wurde
- das Ergebnis des Tests
- Wann der Test durchgeführt wurde

Außer dem Protokoll gibst du auch die Script-Dateien ab,
in denen die Funktionen implementiert sind.


### UE_5.0_1: Idealgewicht

In deinem Alter liegt der ideale Wert für den BMI bei ca. 21.
Schreibe eine Funktion `idealgewicht(groesse)`, die das Idealgewicht
für eine Körpergröße berechnet, so dass der BMI 21 beträgt.
Man übergibt der Funktion die Körpergröße in cm 
und sie gibt das Idealgewicht in kg zurück.

### UE_5.0_2: Körperoberfläche

Die Körperoberfläche ist ein wichtiger Wert in der Medizin,
um z.B. die Dosierung von Medikamenten zu berechnen
oder um den Schweregrad von Verbrennungen zu bestimmen.

Die Körperoberfläche kann mit der 
[Gehan-George-Formel](https://de.wikipedia.org/wiki/K%C3%B6rperoberfl%C3%A4che)
 berechnet werden.

Schreibe eine Funktion `koerperoberflaeche(m, l)`, 
welche die Körperoberfläche nach der
[Gehan-George-Formel](https://de.wikipedia.org/wiki/K%C3%B6rperoberfl%C3%A4che)
berechnet und zurückgibt.

### UE_5.0_3: Temperaturumrechnung

Schreibe eine Funktion `celsius2fahrenheit(celsius)`,
die eine Temperatur von Grad Celsius auf 
[Fahrenheit](https://de.wikipedia.org/wiki/Grad_Fahrenheit)
umrechnet.

Schreibe eine Funktion `fahrenheit2celsius(fahrenheit)`,
die eine Temperatur von Grad Fahrenheit auf Celsius umrechnet.

### UE_5.0_4: Kugelvolumen

Schreibe eine Funktion `kugelvolumen(radius)`,
die das Volumen einer Kugel mit dem Radius `radius` berechnet.

### UE_5.0_5: Freier Fall

Schreibe eine Funktion `freier_fall(hoehe)`,
welche die Fallzeit eines Körpers berechnet, der aus einer Höhe `hoehe` fällt
(Höhe in Meter, Fallzeit in Sekunden).
Die Fallzeit berechnet sich nach der Formel:

$$
t = \sqrt{\frac{2 \cdot h}{g}}
$$

wobei $g = 9.81 \frac{m}{s^2}$ die Erdbeschleunigung ist.

*(Hier wird der Luftwiderstand vernachlässigt.)*

### UE_5.0_6: Vermehrung von Bakterien

Schreibe eine Funktion `bakterienzahl(n0, p, t)`,
welche die Anzahl der Bakterien nach einer Zeit `t` berechnet.
Die Anzahl der Bakterien `n` berechnet sich nach der Formel:

$$
n = n_0 \cdot (1 + \frac{p}{100})^t
$$

wobei `n0` die Anfangszahl der Bakterien, `p` die Vermehrungsrate pro Stunde in %
und `t` die Zeit in Stunden ist.

### UE_5.0_7: Energieverbrauch beim Bergsteigen

Schreibe eine Funktion `energieverbrauch(m, h)`,
welche den Energieverbrauch beim Bergsteigen berechnet.
Die Funktion erhält die Masse `m` des Bergsteigers in kg,
die Höhendifferenz `h` in Meter und gibt den Energieverbrauch in kJ zurück.

Der Energieverbrauch berechnet sich nach der Formel:

$$
E = m \cdot g \cdot h
$$

wobei $g = 9.81 \frac{m}{s^2}$ die Erdbeschleunigung ist.

*(Hier wird nur die potentielle Energie berücksichtigt, 
welche durch den Gewinn an Höhe verbraucht wird. 
In Wirklichkeit wird der Bergsteiger deutlich mehr Energie benötigen.)*







[<<](../skriptum/5.0_Funktionen.md)