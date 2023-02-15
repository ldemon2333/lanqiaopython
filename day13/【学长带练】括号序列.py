class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b

    def mul(self, a, b):
        return (a * b) % self.mod if self.mod else a * b

ring = ModCalculation(int(1e9) + 7)


def ctx_reverse(s):
    res = ''

    for c in s:
        res += ')' if c == '(' else '('

    return res[:: -1]


def count(s):
    n = len(s)
    s = ' ' + s

    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        left = s[i] == '('
        dp[i][0] = 0 if left else ring.add(dp[i - 1][0], dp[i - 1][1])

        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] if left else ring.add(dp[i - 1][j + 1], dp[i][j - 1])

    for cnt in dp[n]:
        if cnt:
            return cnt


if __name__ == '__main__':
    s = input()
    print(ring.mul(count(s), count(ctx_reverse(s))))
