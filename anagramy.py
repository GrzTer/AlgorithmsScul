"""
Zadanie: ANA
Anagramy
    Ćwiczenia. Dostępna pamięć: 32 MB 02.11.2016
    Anagramem słowa k nazywamy takie słowo l, które składa się z takich samych liter, co słowo k lecz w
    dowolnej kolejności.
Wejście:
    W dwóch wierszach standardowego wejścia podano słowa k oraz l o długości do 200 znaków,
    złożone wyłącznie z małych liter alfabetu angielskiego.
Wyjście:
    W jedynym wierszu standardowego wyjścia należy wypisad TAK, jeśli słowo l jest anagramem słowa
    k, bądź NIE, jeśli słowo l nie jest anagramem słowa k.
Przykłady:
    Dla danych wejściowych:
        `takt`
        `tkat`
        `aaa`
        `aaa`
    poprawnym wynikiem jest:
        `TAK`
        `TAK`
"""

def czy_anagram(k: str, l: str) -> str: return ("TAK" if sorted(k) == sorted(l) else "NIE") if len(k) == len(l) else "NIE"

def czy_anagram_2(k: str, l: str) -> str:
    if len(k) != len(l): return "NIE"


def main() -> None:
    k = input().strip()
    l = input().strip()
    print(czy_anagram(k, l))
if __name__ == "__main__":
    main()
