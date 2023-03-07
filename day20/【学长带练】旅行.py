from fractions import Fraction


int_line = lambda: map(int, input().split())


class UFS:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n + 1))

    def is_root(self, a):
        return a == self.f[a]

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        if not self.is_root(a):
            f = self.f[a]
            self.f[a] = self.find(f)

        return self.f[a]

    def union(self, a, b):                      # a branch, b root
        root_a, root_b = self.find(a), self.find(b)

        if root_a != root_b:
            self.f[root_a] = root_b


class EdgeSet:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add(self, u, v, w):
        if u > v:
            u, v = v, u
        pair = (u, v)

        self.edges.append((w, pair))

    def min_delt(self, a, b):
        n = self.n
        m = float('inf')

        edges = sorted(self.edges)
        size = len(edges)

        weight = lambda k: edges[k][0]
        vertex = lambda k: edges[k][1]

        for i in range(size):
            ufs = UFS(n)

            for j in range(i, size):
                ufs.union(*vertex(j))

                if ufs.is_connected(a, b):
                    w_m, w_M = weight(i), weight(j)
                    m = min(m, Fraction(w_M, w_m))

                    break

        return m


if __name__ == '__main__':
    n, m = int_line()
    edges = EdgeSet(n)

    for _ in range(m):
        edges.add(*int_line())

    ans = edges.min_delt(*int_line())
    print('IMPOSSIBLE' if ans == float('inf') else ans)