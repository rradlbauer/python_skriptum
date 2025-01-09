# UE_8.0 Bedingte Anweisungen - Übungen

### UE_8.0_1: Körpertemperatur

Erstelle eine Funktion, welcher man die Körpertemperatur übergeben kann.
Die Funktion soll dann einen Text zurückgeben, welcher die Temperatur beschreibt.

Die Beschreibung soll folgendermaßen aussehen:

- unter 36.0: "Unterkühlung"
- unter 37.5: "Normaltemperatur"
- unter 38.0: "erhöhte Temperatur"
- ab 38.0: "Fieber"

### UE_8.0_2: Teiler

Erstelle eine Funktion, welcher zwei Zahlen übergeben werden.
Die Funktion soll dann zurückgeben, ob eine der beiden Zahlen durch die andere teilbar ist.
Wenn das der Fall ist, soll die Funktion `True` zurückgeben, ansonsten `False`.
Mit dem Modulo-Operator kannst du prüfen, ob eine Zahl durch eine andere teilbar ist:

```python
if zahl1 % zahl2 == 0:
    print("teilbar")
else:
    print("nicht teilbar")
```

### UE_8.0_3: Schaltjahr

Erstelle eine Funktion, welcher man eine Jahreszahl übergeben kann.
Die Funktion soll dann `True` zurückgeben, wenn das Jahr ein Schaltjahr ist, ansonsten `False`.
Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist.
Jedoch ist ein Jahr kein Schaltjahr, wenn es durch 100 teilbar ist.
Es sei denn, das Jahr ist durch 400 teilbar, dann ist es doch ein Schaltjahr.

Teste deine Funktion mit folgenden Jahreszahlen:
* 2025 ist kein Schaltjahr
* 2024 ist ein Schaltjahr
* 1900 ist kein Schaltjahr
* 2000 ist ein Schaltjahr

### UE_8.0_4: Datumsprüfung

Erstelle eine Funktion, welcher man drei Zahlen übergeben kann.
Die Zahlen sollen ein Datum darstellen: Tag, Monat, Jahr.
Die Funktion soll dann `True` zurückgeben, wenn das Datum korrekt ist, ansonsten `False`.

Überlege selbst, welche Bedingungen für ein korrektes Datum gelten.

### UE_8.0_5: Body Mass Index mit Bewertung

| Alter | BMI Männer | BMI Frauen |
|-------|------------|------------|
| 19-24 | 19-24      | 18-23      |
| 25-34 | 20-25      | 19-24      |
| 35-44 | 21-26      | 20-25      |
| 45-54 | 22-27      | 21-26      |
| 55-64 | 23-28      | 22-27      |
| 65+   | 24-29      | 23-28      |

*[Quelle](https://plakos-akademie.de/bmi-rechner/)*

Diese Tabelle zeigt die Normalwerte für den Body Mass Index (BMI) für Frauen und Männer
in Abhängigkeit vom Alter.

Zum Beispiel ist ein 30-jähriger Mann mit einem BMI unter 20 untergewichtig,
von 20 bis 25 normalgewichtig und über 25 übergewichtig.

Erstelle eine Funktion, welcher man das Geschlecht, 
das Alter, die Größe in cm und das Gewicht in kg übergeben kann.
Die Funktion soll dann den BMI berechnen und eine Bewertung 
entsprechend dieser Tabelle zurückgeben. 
Die Funktion soll also einen der folgenden Texte zurückgeben:
`'untergewichtig'`, `'normalgewichtig'`, `'übergewichtig'`.

### UE_8.0_6: Dreiecksungleichung

Erstelle eine Funktion, welcher man drei Zahlen übergeben kann.
Die Zahlen sollen die Längen der Seiten eines Dreiecks darstellen.
Die Funktion soll dann `True` zurückgeben, wenn die Dreiecksungleichung erfüllt ist, 
ansonsten `False`.

Die Dreiecksungleichung besagt, 
dass die Summe der Längen zweier Seiten eines Dreiecks
immer größer sein muss als die Länge der dritten Seite.

### UE_8.0_7: Vom RNA-Code zur Aminosäure

In den Mitochondrien einer Zelle werden aus dem genetischen Code der RNA
Aminosäuren hergestellt.
Immer 3 Basen des genetischen Codes bilden ein sogenanntes Codon, 
welches für eine Aminosäure steht.
Aus welchem Codon welche Aminosäure entsteht, kann man von der Codon-Sonne ablesen.
Das wird z.B. hier genauer erklärt:
[StudyFlix Codesonne](https://studyflix.de/biologie/codesonne-2539).

Man beginnt immer in der Mitte der Sonne und liest dann die Aminosäure ab,
welche durch die 3 Basen des Codons codiert wird.
Z.B. steht das Codon `GCA` für die Aminosäure `Ala` (Alanin).

<a title="Mouagip, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Aminoacids_table.svg"><img width="512" alt="Aminoacids table" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Aminoacids_table.svg/512px-Aminoacids_table.svg.png?20210405175054"></a>

Erstelle eine Funktion `transkription`, welcher man 3 Basen übergeben kann.
Die Funktion soll dann die entsprechende Aminosäure zurückgeben.

Beispiel: `transkription('G', 'C', 'A')` soll den String `'Ala'` zurückgeben.
`transkription('U', 'G', 'A')` soll den String `'Stop'` zurückgeben.





[<<](../skriptum/8.0_IfElse.md)
