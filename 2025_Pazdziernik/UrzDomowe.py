class Urzadzenie:
    def pokaz_komunikat(self, komunikat: str) -> None:
        print(komunikat)
class Pralka(Urzadzenie):
    def __init__(self):
        self.__numer_programu = 0

    def ustaw_program(self, numer_programu) -> int:
        if 1 <= numer_programu <= 12: self.__numer_programu = numer_programu
        else: self.__numer_programu = 0
        return self.__numer_programu

class Odkurzacz(Urzadzenie):
    def __init__(self) -> None: 
        self.__stan = False

    def on(self) -> None:
        if not self.__stan:
            self.__stan = True
            super().pokaz_komunikat("Odkuracz włączono")
    

    def off(self) -> None:
        if self.__stan:
            self.__stan = False
            super().pokaz_komunikat("Odkuracz wyłączono")


def main() -> None:
    pralka = Pralka()
    odkurzacz = Odkurzacz()
    pralka.pokaz_komunikat(f"Wprowadzony numer programu: {2}. Ustawiono program: {pralka.ustaw_program(2)}")
    if pralka.ustaw_program(13) == 0:
        pralka.pokaz_komunikat(f"Wprowadzony numer programu: {13}. Niepoprawny numer programu.")


    odkurzacz.on()
    odkurzacz.on()
    odkurzacz.on()

    odkurzacz.pokaz_komunikat("Odkurzac wyładowal się")

    odkurzacz.off()
    odkurzacz.off()

if __name__ == "__main__":
    main()