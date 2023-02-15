def linear_sieve(n):            # primes in [2, n]
    is_prime, primes = [True] * (n + 1), []

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return primes


n = int(input())
primes_rev = linear_sieve(n)[:: -1]


def max_factor(n):
    for p in primes_rev:
        if n % p == 0:
            return p


def x_lower(n):
    if n in primes_rev:
        return 0

    return n + 1 - max_factor(n)


def mim_x():
    if n == 1:
        return -1

    lower = x_lower(n)

    if lower == 0:
        return -1

    x_min = float('inf')

    for target in range(lower, n):
        x_l = x_lower(target)

        if x_l:
            x_min = min(x_min, x_l)
        else:
            x_min = min(x_min, target)

    return x_min


print(mim_x())