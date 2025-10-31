import random

def main() -> None:
    while True:
        n = int(input("Ile kostek chcesz rzucić?(3 - 10)\n"))
        if n < 3 or n > 10:
            print("Nieprawidłowa liczba kostek")
        else:
            break
    while True:
        wynik = 0
        for i in range(1, n + 1):
            j = random.randint(1,6)
            print(f"Kostka {i}: {j}")
            wynik += j
        print(f"Liczba uzyskanych punktów: {wynik}")
        print("Jeszcze raz? (t/n)")
        if input() == 'n':
            break

if __name__ == "__main__":
    main()