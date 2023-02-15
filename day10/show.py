class UFS:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n + 1))

        self.size = [1] * (n + 1)
        self.dist = [0] * (n + 1)

    def is_root(self, a):
        return a == self.f[a]

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        if not self.is_root(a):
            f = self.f[a]
            self.f[a] = self.find(f)

            self.dist[a] += self.dist[f]

        return self.f[a]

    def union(self, a, b, s):                      # a branch, b root
        root_a, root_b = self.find(a), self.find(b)

        if root_a != root_b:
            self.f[root_a] = root_b

            self.dist[root_a] = s + self.dist[b] - self.dist[a]                    # update dist
            self.size[root_b] += self.size[root_a]

    def get_roots(self):
        return [i for i in range(1, self.n + 1) if self.is_root(i)]

    def get_size(self, a):
        root = self.find(a)
        return self.size[root]

    def get_dist(self, a):
        self.find(a)
        return self.dist[a]

    def calc_dist(self, a, b):
        if not self.is_connected(a, b):
            return -1

        return self.dist[a] - self.dist[b]


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    ufs = UFS(n)

    for _ in range(m):
        l, r, s = map(int, input().split())
        ufs.union(l - 1, r, s)

    for _ in range(q):
        l, r = map(int, input().split())
        
        print(ufs.calc_dist(l - 1, r) if ufs.is_connected(l - 1, r) else 'UNKNOWN')