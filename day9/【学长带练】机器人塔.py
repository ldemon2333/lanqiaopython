calc_n = lambda a, b: int((2 * (a + b) + 0.25) ** 0.5 - 0.5)


def last(i, j):
    mask = (1 << i) - 1
    back = (j << 1) & mask
    return (back ^ j) >> 1


def count(i, j):
    mask = 1 << i

    s = bin(mask | j)[2 + 1:]

    zero = s.count('0')

    return zero, len(s) - zero


def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


dp = [[(0, 0)]]

if __name__ == '__main__':
    pair = tuple(map(int, input().split()))
    n = calc_n(*pair)

    for i in range(1, n + 1):
        dp.append([])

        for j in range(1 << i):
            last_index = last(i, j)
            last_cnt = dp[i - 1][last_index]

            cnt = count(i, j)
            dp[i].append(add(*last_cnt, *cnt))

    print(dp[n].count(pair))