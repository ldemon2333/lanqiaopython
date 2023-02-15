def bound(true, l, r):      # last number makes true in [l, r)
    if r - l == 0 or not true(l):
        return -1           # no number makes true
    
    while r - l > 1:
        m = (l + r) // 2

        if true(m):
            l = m
        else:
            r = m

    return l


def count(n):
    cnt = 0

    while n:
        n //= 5

        cnt += n

    return cnt


if __name__ == '__main__':
    k = int(input())

    n = bound(lambda i: count(i) < k, 1, int(1e19)) + 1

    print(n if count(n) == k else -1)