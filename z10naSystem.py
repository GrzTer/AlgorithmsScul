RESZTY = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F'
          ]

def z10naSystem(liczba: int, system: int) -> str:
    wynik: str =  ""
    while liczba > 0:
        reszta = liczba % system
        wynik = RESZTY[reszta] + wynik
        liczba //= system
    return wynik

def main() -> None:
    print(z10naSystem(54, 3))

if __name__ == "__main__":
    main()


# -5

# 5

# 101

# 0000 0101 /// fill
# 1111 1010 /// swap
# 1111 1011 /// add 1
