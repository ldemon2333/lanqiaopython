split_line = lambda: map(int, input().split())

if __name__ == '__main__':
    t, m = split_line()
    w_v = [(0, 0)] + [tuple(split_line()) for _ in range(m)]

    dp = [[0] * (t + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, t + 1):
            dp[i][j] = dp[i - 1][j]

            w, v = w_v[i]
            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

    print(dp[m][t])
