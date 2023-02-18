n, m = map(int, input().split())

matrix = [input() for _ in range(n)]


def is_bomb(x, y):
    return matrix[x][y] == '*'


def search(x, y):
    if is_bomb(x, y):
        return '*'

    cnt = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):

            if 0 <= i < n and 0 <= j < m:
                if is_bomb(i, j):
                    cnt += 1
    
    return str(cnt)


for i in range(n):
    s = ''

    for j in range(m):
        s += search(i, j)
    
    print(s)