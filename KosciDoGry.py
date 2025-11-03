import random


def losuj_kosci(n: int) -> list[int]:
    rzuty = [random.randint(1, 6) for _ in range(n)]
    return rzuty


def licz_punkty(lista_rzutow: list[int]) -> int:

    licznik = {}
    for rzut in lista_rzutow:
        if rzut in licznik:
            licznik[rzut] += 1
        else:
            licznik[rzut] = 1
    wynik = 0
    for oczka, ilosc in licznik.items():
        if ilosc >= 2:
            wynik += oczka * ilosc
    return wynik


def main() -> None:
    while True:
        try:
            n = int(input("Ile kostek chcesz rzucić? (3 - 10)\n"))
            if n < 3 or n > 10:
                print("Nieprawidłowa liczba kostek. Wprowadz liczbę od 3 do 10.")
            else:
                break
        except:
            print("To nie jest poprawna liczba. Spróbuj ponownie.")

    while True:
        rzuty = losuj_kosci(n)
        for i in range(len(rzuty)):
            print(f"Kostka {i + 1}: {rzuty[i]}")
        wynik = licz_punkty(rzuty)
        print(f"Liczba uzyskanych punktów: {wynik}")
        print("Jeszcze raz? (t/n)")
        czy_kontynuować = input().lower()
        if czy_kontynuować == "n":
            break
        elif czy_kontynuować == "t":
            continue


if __name__ == "__main__":
    main()
