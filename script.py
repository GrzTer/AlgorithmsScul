def Zad_210(dec_num: int) -> str:
    binary_n = bin(dec_num)[2:]
    sum_digits = binary_n.count('1')
    binary_sum = bin(sum_digits)[2:]
    return f"{binary_n} {binary_sum}"
def binary_to_decimal(binary_string: str) -> int:
    decimal_number = 0
    for i, digit in enumerate(binary_string[::-1]):
        decimal_number += int(digit) * (2 ** i)
    return decimal_number

def main() -> None:
    ...
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()