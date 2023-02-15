class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b

    def sum(self, iterable):
        s = 0
        for i in iterable:
            s = self.add(s, i)
        return s

    def mul(self, a, b):
        return (a * b) % self.mod if self.mod else a * b

    def quick_power(self, a, n):
        res = 1

        while n:
            if n & 1:
                res = self.mul(res, a)

            a = self.mul(a, a)
            n >>= 1

        return res


class UFS:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n + 1))

        self.size = [1] * (n + 1)
        self.dist = [0] * (n + 1)   # 节点与父节点异或值

    def is_root(self, a):
        return a == self.f[a]

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        if not self.is_root(a):
            f = self.f[a]
            self.f[a] = self.find(f)

            self.dist[a] ^= self.dist[f]

        return self.f[a]

    def union(self, a, b, xor):     # a branch, b root
        root_a, root_b = self.find(a), self.find(b)

        dist_xor = self.dist[a] ^ self.dist[b]
        different = xor ^ dist_xor

        if root_a == root_b and different:
            return True             # illegal

        if root_a != root_b:
            self.f[root_a] = root_b

            self.dist[root_a] ^= different

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


mod_calc = ModCalculation(int(1e9))
points = []


def get_xor(x, y, c, start):
    num = (x - 1) * (y - 1)
    xor = c ^ start

    if num % 2:
        return xor ^ 1
    return xor


def count(n, m, start):
    ufs = UFS(n + m)
    ufs.f[1 + n] = 1

    for x, y, c in points:
        xor = get_xor(x, y, c, start)
        if ufs.union(x, y + n, xor):
            return 0

    return mod_calc.quick_power(2, len(ufs.get_roots()) - 1)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    start = -1

    for _ in range(k):
        x, y, c = map(int, input().split())

        if x == 1 and y == 1:
            start = c
        else:
            points.append((x, y, c))

    print(mod_calc.add(count(n, m, 0), count(n, m, 1)) if start == -1 else count(n, m, start))