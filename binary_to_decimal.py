reszty = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def z10naSystem(liczba, system):
    wynik = ""
    while liczba > 0:
        reszta = liczba % system
        wynik = reszty[reszta] + wynik
        liczba = liczba //system
    return wynik

print(z10naSystem(30, 16))


def zSystemNa10(tekst, system):
    # schemat Hornera
    wynik = 0
    for znak in tekst:
        wynik = wynik * system + reszty.index(znak)
    return wynik
        
print(zSystemNa10("1E", 16))  







def binary_to_decimal(binary_string: str) -> 
int:
    decimal_number = 0
    for i, digit in enumerate(binary_string[::-1]):
        decimal_number += int(digit) * (2**i)
    return decimal_number


# def binary_to_decimal(s: str) -> int: return sum((ord(c) - ord('0')) << (len(s) - i - 1) for i, c in enumerate(s)) if all(c in '01' for c in s) else exec('raise ValueError("Błąd: Nieprawidłowy ciąg binarny")')


def main() -> None:
    binary_string = input()
    print(binary_to_decimal(binary_string))


if __name__ == "__main__":
    main()
