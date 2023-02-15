from math import factorial

comb = lambda n, k: factorial(n) // factorial(k) // factorial(n - k)


mod = 10007


def mul(*args):
    res = 1
    for arg in args:
        res = (res * arg) % mod
    return res


if __name__ == '__main__':
    a, b, k, n, m = map(int, input().split())
    print(mul(comb(k, n), a ** n, b ** m))