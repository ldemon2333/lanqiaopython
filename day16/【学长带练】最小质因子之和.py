def sieve(n):
    is_prime, primes = [True] * (n + 1), []

    factors = [0] * (n + 1)

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

            factors[p] = p

            for i in range(p * p, n + 1, p):
                is_prime[i] = False

                if factors[i] == 0:
                    factors[i] = p

    return factors


if __name__ == '__main__':
    N = int(3e6)
    factors = sieve(N)

    s = [0] * (N + 1)
    for i in range(2, N + 1):
        s[i] = s[i - 1] + factors[i]

    for _ in range(int(input())):
        n = int(input())
        print(s[n])