
# **************************************************************************
# nazwa funkcji:
# opis funkcji:
# parametry:
# zwracany typ:
# autor:
# **************************************************************************
# def rozklad_mat(n: int) -> int:
#     dzielnik = 2
#     Lista_dzielnikow = []
#     while n > 1:
#         if n % dzielnik == 0:
#             Lista_dzielnikow.append(dzielnik)
#             n = n // dzielnik
#         else:
#             dzielnik += 1
#     return Lista_dzielnikow

def rozklad_inf(n: int) -> int:
    dzielnik = 2
    lista_dzielnikow = []
    while dzielnik * dzielnik <= n:
        if n % dzielnik == 0:
            lista_dzielnikow.append(dzielnik)
            n = n // dzielnik
        else:
            dzielnik += 1
    if n > 1:
        lista_dzielnikow.append(n)
    return lista_dzielnikow

def main() -> None:
    # print(*rozklad_mat(100), sep="*")
    # print(*rozklad_inf(1000000007), sep="*")
    k = int(input())
    for i in range(k):
        n = int(input())
        print(*rozklad_inf(n), sep="*")
if __name__ == "__main__": main()


