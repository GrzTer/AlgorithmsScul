def binary_to_decimal(binary_string: str) -> int:
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
