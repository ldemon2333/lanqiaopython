n, m = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


def search(x, y):
    if matrix[x][y]:
        return 9

    cnt = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < n and 0 <= j < m:
                cnt += matrix[i][j]
    
    return cnt


map = [[search(i, j) for j in range(m)] for i in range(n)]

for l in map:
    print(*l)