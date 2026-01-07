# Ausgewählte Musterlösugen

In diesem Anhang befinden sich Musterlösungen zu ausgewählten Übungen.

Es wird empfohlen, die Übungen zunächst selbst zu bearbeiten und
erst bei Bedarf einen Blick in die Musterlösungen zu werfen.

### Musterlösung UE_23.0_3: Impfpass

````python
from datetime import date

class Impfung:
    def __init__(self, impfstoff: str, dosis: float, arzt: str):
        self.impfstoff: str = impfstoff
        self.dosis: float = dosis  # in ml
        self.arzt: str = arzt
        # Datum wird nicht übergeben, sondern auf das aktuelle Datum gesetzt
        self.datum = date.today()


class Impfpass:
    def __init__(self, patient: str):
        self.patient: str = patient
        self.impfungen: list[Impfung] = []  # zu Beginn ist die Liste leer

    def neu(self, impfung: Impfung) -> None:
        """
        Neue Impfung eintragen, wenn sie noch nicht vorhanden ist.
        :param impfung: Impfung-Objekt, das eingetragen werden soll
        :raises ValueError: wenn die Impfung bereits eingetragen ist
        """
        for i in self.impfungen:
            if i.impfstoff == impfung.impfstoff and i.datum == impfung.datum:
                # raise löst eine Exception aus - diese kann mit try/except abgefangen werden.
                raise ValueError("Diese Impfung wurde bereits eingetragen.")
        self.impfungen.append(impfung)

    def impfstoffe(self) -> list[str]:
        """
        Gibt eine Liste aller verabreichten Impfstoffe zurück.
        :return: Liste der Impfstoffe ohne Duplikate
        """
        # alle Impfstoffe in einem Set sammeln, um Duplikate zu vermeiden
        # dann in eine Liste umwandeln und zurückgeben
        return list({impfung.impfstoff for impfung in self.impfungen})

    def suche(self, impfstoff: str) -> list[Impfung]:
        """
        Sucht alle Impfungen mit dem angegebenen Impfstoff.
        :param impfstoff: Name des Impfstoffs, nach dem gesucht werden soll
        :return: Liste der gefundenen Impfungen
        """
        return [impfung for impfung in self.impfungen if impfung.impfstoff == impfstoff]


if __name__ == "__main__":
    # Erstelle Impfpass
    pass1 = Impfpass("Max Mustermann")
    # Füge einige Impfungen hinzu
    # Behandle Exceptions, die beim Hinzufügen auftreten können
    try:

        impfung1 = Impfung("Vaxigrip", 0.3, "Dr. Meier")
        impfung1.datum = date(2019, 10, 23)
        pass1.neu(impfung1)
        impfung2 = Impfung("Comirnaty", 0.5, "Dr. Müller")
        impfung2.datum = date(2021, 5, 1)
        pass1.neu(impfung2)
        impfung3 = Impfung("Vaxigrip", 0.3, "Dr. Schmidt")
        impfung3.datum = date(2020, 11, 5)
        pass1.neu(impfung3)
        impfung4 = Impfung("Vaxigrip", 0.3, "Dr. Schmidt")
        impfung4.datum = date(2021, 10, 15)
        pass1.neu(impfung4)
        impfung5 = Impfung("Comirnaty", 0.5, "Dr. Müller")
        impfung5.datum = date(2022, 5, 1)
        pass1.neu(impfung5)
        impfung6 = Impfung("Priorix", 0.5, "Dr. Müller")
        impfung6.datum = date(2019, 3, 1)
        pass1.neu(impfung6)
        impfung7 = Impfung("Comirnaty", 0.5, "Dr. Müller")
        impfung7.datum = date(2021, 5, 1)
        pass1.neu(impfung7)  # Diese Impfung ist doppelt
    except ValueError as e:
        print(e)

    # Ausgabe der Impfstoffe im Impfpass
    print("Impfstoffe im Impfpass von", pass1.patient + ":")
    for stoff in pass1.impfstoffe():
        print("-", stoff)

    # Suche nach Impfungen eines bestimmten von Benutzer eingegebenen Impfstoffs
    while True:
        impfst = input("Impfstoff: ")
        if impfst == "":
            break
        for impfg in pass1.suche(impfst):
            print(
                f"{impfg.datum}: {impfg.impfstoff} ({impfg.dosis} ml) verabreicht von {impfg.arzt}"
            )

````



