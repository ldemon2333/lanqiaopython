class AdjMatrix:
    def __init__(self, n):
        self.n = n                                  # default 0 and 1 to n vertex
        self.matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            self[i][i] = 0

    def __getitem__(self, item):
        return self.matrix[item]

    def floyd(self):
        n = self.n
        matrix = self.matrix

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


t = 32
n, m = map(int, input().split())

graph = AdjMatrix(n)
dp = [[[False] * (t + 1) for _ in range(n + 1)] for _ in range(n + 1)]


def update(pow, i, j):
    for k in range(1, n + 1):
        if dp[i][k][pow - 1] and dp[k][j][pow - 1]:

            dp[i][j][pow] = True
            graph[i][j] = 1
            return


for _ in range(m):
    u, v = map(int, input().split())

    dp[u][v][0] = True
    graph[u][v] = 1

for pow in range(1, t + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            update(pow, i, j)

graph.floyd()
print(graph[1][n])