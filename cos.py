def sumaD(n: int) -> int:
    w = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            w += i + n // i
        i += 1
    if i * i == n:
        w += i
    return w

def ileD(n: int) -> int:
    i = 1
    w = 0
    while i * i < n:
        if n% i == 0:
            w += 2
        i += 1
    if i * i == n:
        w += 1
    return w
print(ileD(9))

def sumaD_dosk(n: int) -> int:
    w = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            w += i + n // i
        i += 1
    if i * i == n:
        w += i
    return w - n
print(sumaD_dosk(9))