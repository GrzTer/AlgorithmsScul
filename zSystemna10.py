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

def z10naSystem(tekst: str, system: int) -> int: return [sum(RESZTY.index(znak) * (system ** i)) for znak in tekst] # Horner
def main() -> None:
    print(z10naSystem("320", 4))

if __name__ == "__main__":
    main()


# 111101010 = 000010100 = -20

# -5

# 5

# 101

# 0000 0101 /// fill
# 1111 1010 /// swap
# 1111 1011 /// add 1
