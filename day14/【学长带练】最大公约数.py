ls = lambda k: 2 * k
rs = lambda k: 2 * k + 1


class GCDSegmentTree:
    def __init__(self, array):  # element index starts from 0
        from math import gcd

        self.gcd = gcd

        self.n = len(array)
        size = 4 * self.n

        self.array = [0] + array

        self.left, self.right = [0] * size, [0] * size
        self.value, self.tag = [0] * size, [0] * size

        self.build(1, 1, self.n)

    def m(self, k):
        return (self.left[k] + self.right[k]) // 2

    def length(self, k):
        return self.right[k] - self.left[k] + 1

    def push_up(self, k):
        self.value[k] = self.gcd(self.value[ls(k)], self.value[rs(k)])

    def build(self, k, l, r):
        self.left[k], self.right[k] = l, r

        if l == r:
            self.value[k] = self.array[l]
        else:
            m = self.m(k)

            self.build(ls(k), l, m)
            self.build(rs(k), m + 1, r)
            self.push_up(k)

    def _query(self, k, a, b):
        if a <= self.left[k] and self.right[k] <= b:
            return self.value[k]

        res = 0

        m = self.m(k)
        if a <= m:
            res = self.gcd(res, self._query(ls(k), a, b))
        if m < b:
            res = self.gcd(res, self._query(rs(k), a, b))

        return res

    def query(self, a, b):
        return self._query(1, a, b)


class Window:
    def __init__(self, left):
        self.left = left
        self.right = left - 1

    def __len__(self):
        return self.right - self.left + 1

    def push(self):
        self.right += 1

    def pop(self):
        self.left += 1

    def true(self, tree):
        return tree.query(self.left, self.right) == 1


def min_ops(n, a):
    ones = a.count(1)
    if ones:
        return n - ones

    tree = GCDSegmentTree(a)
    window = Window(1)

    m = float('inf')
    for _ in range(n):
        window.push()

        while window.true(tree):
            m = min(m, len(window))

            window.pop()

    return -1 if m == float('inf') else n + m - 2


if __name__ == '__main__':
    print(min_ops(int(input()), [int(x) for x in input().split()]))
