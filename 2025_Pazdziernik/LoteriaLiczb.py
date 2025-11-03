import random

def losuj_w_loterii(n: int) -> None:
    losowania = []
    for i in range(n):
        losowanie = random.sample(range(1, 50), 6)
        losowania.append(losowanie)
        print(f"Losowanie {i+1}: {" ".join(map(str, losowania[i]))}")

    for i in range(1, 50):
        ncount = 0
        for j in range(n):
            ncount += losowania[j].count(i)
        print(f"Wystąpienia liczby {i}: {ncount}")


def main() -> None:
    n = int(input("Ile wygenerować losowań?\n"))
    losuj_w_loterii(n)

if __name__ == "__main__":
    main()