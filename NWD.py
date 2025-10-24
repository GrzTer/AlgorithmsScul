
"""         ----   Iteracyjnie     ---
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


def main() -> None:
    while True:
        a, b = map(int, input("Podaj a > 0 i b > 0 ! po spacji !: ").split())
        if a > 0 and b > 0: break
        print("Wartość a i b muszą być > 0")
    print(f"nwd({a}, {b}) == {nwd(a, b)}")
    # print(nwd_recur(a, b))


if __name__ == "__main__": main()

"""
"""
# *************************************************************************
# nazwa funkcji: nwd
# opis funkcji: Dla dodatnich liczb a i b zwraca największy wspólny dzielnik
# parametry: a - liczba dodatnia na których liczymy nwd
#            b - liczba dodatnia na których liczymy nwd
# zwracany typ: liczba dodatnia a, największy wspólny dzielnik
# autor: 000000000
# **************************************************************************
def nwd(a: int, b: int) -> int:
    while b:
        a , b = b, a % b
    return a


def main() -> None:
    while True:
        a, b = map(int, input("Podaj a > 0 i b > 0 ! po spacji !: ").split())
        if a > 0 and b > 0: break
        print("Wartość a i b muszą być > 0")
    print(f"nwd({a}, {b}) == {nwd(a, b)}")
    # print(nwd_recur(a, b))


if __name__ == "__main__": main()
"""




def nwd_recur(a: int, b: int) -> int:
    if b == 0:
        return a
    return nwd_recur(b, a % b)

# def nwd_recur(a: int, b: int) -> int: return a if b==0 else nwd_recur(b, a % b)



def main() -> None:
    while True:
        a, b = map(int, input("Podaj a > 0 i b > 0 ! po spacji !: ").split())
        if a > 0 and b > 0: break
        print("Wartość a i b muszą być > 0")
    print(f"nwd({a}, {b}) == {nwd_recur(a, b)}")


if __name__ == "__main__": main()