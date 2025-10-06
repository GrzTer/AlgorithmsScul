"""
System 36
Dostępna pamięć: 32MB
    Janek sprawdza przydatność obliczeń w różnych systemach obliczeń. Stwierdził, że
    korzystając z cyfr i dużych liter alfabetu łacińskiego może korzystać nawet z systemu
    trzydziestoszóstkowego! Próbuje teraz napisać program, który szybko przeliczałby wartości
    pomiędzy dowolnymi systemami liczbowymi.
Wejście
    Pierwszy wiersz zawiera trzy liczby: X, Y i Z, gdzie X jest liczbą zapisaną w systemie
    o podstawie Y (wartość X nie przekracza 1015 w systemie dziesiętnym). Z jest podstawą
    systemu, na który należy zamienić liczbę X (1 < Y, Z < 37).
Wyjście
    Jedna liczba całkowita - zapis X w systemie o podstawie Z.
Przykład
    Wejście
        `37826876 10 36`
    Wyjście
        `MIREK`
"""
# x,y,z=input().split()
# y,z=int(y),int(z)
# dec=int(x,y)
# d="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# r=""
# while dec:dec,m=divmod(dec,z);r=d[m]+r
# print(r or "0")





def main() -> None:
    x, y, z = input().split()

    y, z = int(y), int(z)

    dec = int(x, y)

    dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while dec:dec, m=divmod(dec, z); res=dig[m] + res
    print(res or 0)

if __name__ == '__main__':
    main()