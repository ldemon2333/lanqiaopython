from copy import deepcopy


int_matrix = lambda n: [[int(x) for x in input().split()] for _ in range(n)]


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


def floyd(matrix):
    n = len(matrix)  # vertex from 0 to n-1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


n, q = map(int, input().split())
graph, lower = int_matrix(n), int_matrix(n)

DAY = n * (n - 1) // 2 * int(1e5)


def improve(matrix, i):
    for j in range(n):
        if matrix[i][j] > lower[i][j]:
            matrix[i][j] -= 1
            matrix[j][i] -= 1


def check(days):
    matrix = deepcopy(graph)

    for day in range(days):
        improve(matrix, day % n)

    floyd(matrix)
    p = sum(sum(l) for l in matrix)

    return p > q


d = bound(check, 0, DAY) + 1
print(-1 if d == DAY else d)