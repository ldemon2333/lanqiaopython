N = 100000
cnt = [0] * (N + 1)       # cnt[i] = number of elements <= i

less = lambda i: cnt[i - 1] if i else 0
more = lambda i: cnt[N] - cnt[i]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]

    for x in a:
        cnt[x] += 1

    for i in range(1, N + 1):
        cnt[i] += cnt[i - 1]

    for i in range(N + 1):
        new_less = less(i) - 1
        if new_less >= more(i):
            min_law = i
            break

    for x in a:
        print(0 if less(x) >= more(x) else min_law - x, end = " ")