mod = int(1e9) + 7


if __name__ == '__main__':
    n = int(input())
    A = [0] + [int(x) for x in input().split()]

    dp = [0] * (n + 1)
    dp[0] = 1

    for r in range(1, n + 1):
        M, m = A[r], A[r]

        for l in range(r, 0, -1):
            M, m = max(M, A[l]), min(m, A[l])

            if M - m == r - l:
                dp[r] = (dp[r] + dp[l - 1]) % mod

    print(dp[n])
