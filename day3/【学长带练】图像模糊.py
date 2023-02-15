n, m = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


def pooling(x, y):
    s = 0
    cnt = 0

    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):

            if 0 <= i < n and 0 <= j < m:
                s += matrix[i][j]
                cnt += 1

    return s // cnt


# img = [[pooling(i, j) for j in range(m)] for i in range(n)]


img = []
for i in range(n):
    img.append([])
    for j in range(m):
        img[-1].append(pooling(i, j))
        

for l in img:
    print(*l)