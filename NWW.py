
# **************************************************************************
# nazwa funkcji: nwd
# opis funkcji: Dla dodatnich liczb a i b zwraca największy wspólny dzielnik
# parametry: a - liczba dodatnia na których liczymy nwd
#            b - liczba dodatnia na których liczymy nwd
# zwracany typ: liczba dodatnia a, największy wspólny dzielnik
# autor: 000000000
# **************************************************************************
def nwd(a: int, b: int) -> int:
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

def nww()


def main() -> None:
    while True:
        a, b = map(int, input("Podaj a > 0 i b > 0 ! po spacji !: ").split())
        if a > 0 and b > 0: break
        print("Wartość a i b muszą być > 0")
    print(f"nwd({a}, {b}) == {nwd(a, b)}")
    # print(nwd_recur(a, b))


if __name__ == "__main__": main()


