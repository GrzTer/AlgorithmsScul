def Zad_210(dec_num: int) -> str:
    binary_n = bin(dec_num)[2:]
    sum_digits = binary_n.count('1')
    binary_sum = bin(sum_digits)[2:]
    return f"{binary_n} {binary_sum}"

def main() -> None:
    dec_num = int(input().strip())
    print(Zad_210(dec_num))

if __name__ == '__main__':
    main()