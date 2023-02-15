def sqrt(x):
    return int(x ** 0.5)


def is_square(n):
    root = sqrt(n)

    return n == root * root


def upper(k, n):
    return sqrt(n / k) + 1


def loop(n):
    for a in range(upper(4, n)):
        i = a * a

        for b in range(a,  upper(3, n)):
            j = b * b + i

            for c in range(b, upper(2, n)):
                k = c * c + j

                d_square = n - k
                if d_square >= c * c:
                    if is_square(d_square):
                        d = sqrt(d_square)
                        
                        return a, b, c, d


if __name__ == '__main__':
    print(*loop(int(input())))