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

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    self[j][k] = min(self[j][k], self[j][i] + self[i][k])

    def prim(self):
        n = self.n
        m = 0

        dist = [float('inf')] * (n + 1)
        mst = set()

        def update(u):
            mst.add(u)
            dist[u] = 0

            for v in range(1, n + 1):
                dist[v] = min(dist[v], self[u][v])

        def next():
            u = 0

            for i in range(1, n + 1):
                if i not in mst:
                    if dist[i] < dist[u]:
                        u = i

            return u

        update(1)

        for _ in range(n - 1):
            u = next()

            if u == 0:
                return

            m = max(m, dist[u])
            update(u)

        return m


points = [(0, 0)]


def dist(p1, p2):
    x1, y1 = points[p1]
    x2, y2 = points[p2]

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == '__main__':
    m = int(input())
    monkeys = [int(x) for x in input().split()]

    n = int(input())
    graph = AdjMatrix(n)

    for _ in range(n):
        points.append(tuple(int(x) for x in input().split()))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], dist(i, j))

    d = graph.prim()
    print(sum(1 for x in monkeys if x >= d))