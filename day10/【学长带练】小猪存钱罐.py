class UFS:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n + 1))
        self.size = [1] * (n + 1)

    def is_root(self, x):
        return x == self.f[x]

    def find(self, x):
        if not self.is_root(x):
            self.f[x] = self.find(self.f[x])

        return self.f[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.f[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        root = self.find(x)
        return self.size[root]

    def group_roots(self):
        return [i for i in range(1, self.n + 1) if self.is_root(i)]


if __name__ == '__main__':
    n = int(input())
    ufs = UFS(n)

    for a in range(1, n + 1):
        b = int(input())

        ufs.union(a, b)

    print(len(ufs.group_roots()))