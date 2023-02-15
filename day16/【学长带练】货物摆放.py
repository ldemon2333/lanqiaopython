def break_factor(n):
    sqrt = int(n ** 0.5)

    factors = [sqrt]

    if n // sqrt != sqrt:
        factors.append(n // sqrt)

    for i in range(1, sqrt):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors


if __name__ == '__main__':
    n = 2021041820210418
    factors = sorted(break_factor(n))
    size = len(factors)
    cnt = 0

    for a in factors:
        i = a

        for b in factors:
            j = b * i

            if j > n:
                break

            for c in factors:
                k = c * j

                if k > n:
                    break

                if k == n:
                    cnt += 1

    print(cnt)