from collections import deque


C, U = [0], [0]


class AdjList:
    def __init__(self, n):
        self.n = n
        self.list = [{} for _ in range(n + 1)]  # default 0 and 1 to n vertex

        self.degree = [0] * (n + 1)

    def __getitem__(self, item):
        return self.list[item]

    def add_edge(self, u, v, w):
        adj = self[u]

        if v not in adj:
            adj[v] = w
            self.degree[v] += 1
        else:
            adj[v] = min(adj[v], w)

    def topsort(self):
        n = self.n
        degree = self.degree

        q = deque()

        for i in range(1, n + 1):
            if degree[i] == 0:
                q.append(i)
            else:
                C[i] -= U[i]

        while q:
            layer = q.copy()

            for _ in range(len(q)):
                u = q.popleft()

                for v, w in self[u].items():
                    degree[v] -= 1

                    C[v] += C[u] * w

                    if degree[v] == 0:
                        q.append(v)

                        if C[v] < 0:
                            C[v] = 0

        return layer


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = AdjList(n)

    for _ in range(n):
        c, u = map(int, input().split())
        C.append(c), U.append(u)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)

    layer = [f'{u} {C[u]}' for u in graph.topsort() if C[u] > 0]

    print(*layer if layer else ['NULL'], sep='\n')