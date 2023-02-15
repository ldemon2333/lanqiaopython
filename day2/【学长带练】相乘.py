N = int(1e9)

div, mod = N + 7, N - 1


if __name__ == '__main__':
    q = 0
    while True:
        up = div * q + mod

        n = up // 2021

        if n * 2021 == up:
            print(n)
            break

        q += 1
