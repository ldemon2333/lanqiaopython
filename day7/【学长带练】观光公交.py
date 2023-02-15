n, m, k = map(int, input().split())
D = [0] + [int(x) for x in input().split()]
T, A, B = [], [], []

last = [0] * n
people = [0] * n
arrive = [0] * n


def update_arrive():
    for i in range(1, n):
        arrive[i] = D[i] + max(arrive[i - 1], last[i - 1])


def count_time():
    cnt = 0
    for i in range(m):
        b = B[i]
        cnt += arrive[b] - T[i]
    return cnt


def calc_reduce():
    reduce = people.copy()
    
    for i in range(n - 2, 0, -1):
        if arrive[i] > last[i]:
            reduce[i] += reduce[i + 1]
    return reduce


def most_reduce():
    reduce = calc_reduce()

    p = 0
    for i in range(1, n):
        if D[i] and reduce[i] > reduce[p]:
            p = i
    return p


if __name__ == '__main__':
    for _ in range(m):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a - 1)
        B.append(b - 1)

    for t, a, b in zip(T, A, B):
        last[a] = max(last[a], t)

        people[b] += 1

    update_arrive()
    for _ in range(k):
        D[most_reduce()] -= 1

        update_arrive()

    print(count_time())