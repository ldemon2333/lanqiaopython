class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def get_mod(self, a):
        return a % self.mod if self.mod else a

    def add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b

    def sum(self, iterable):
        s = 0
        for i in iterable:
            s = self.add(s, i)
        return s

    def mul(self, a, b):
        return (a * b) % self.mod if self.mod else a * b

    def power(self, a, n):
        res = 1

        while n:
            res = self.mul(res, a)

        return res

    def quick_power(self, a, n):
        res = 1

        while n:
            if n & 1:
                res = self.mul(res, a)

            a = self.mul(a, a)
            n >>= 1

        return res


ring = ModCalculation(571373)

ls = lambda k: 2 * k
rs = lambda k: 2 * k + 1


class SegmentTree:
    def __init__(self, array):  # element index starts from 0
        self.n = len(array)
        self.size = 4 * self.n

        self.array = [0] + array

        self.left, self.right = [0] * self.size, [0] * self.size
        self.value = [0] * self.size

        self.add_tag = [0] * self.size
        self.mul_tag = [1] * self.size

        self.build(1, 1, self.n)

    def m(self, k):
        return (self.left[k] + self.right[k]) // 2

    def length(self, k):
        return self.right[k] - self.left[k] + 1

    def set_update(self, cmd):
        self.update = self.update_add if cmd == 2 else self.update_mul

    # def update(self, k, delt):
    #     # self.tag[k] += delt
    #     # self.value[k] += delt * self.length(k)
    #     pass
    
    def update_add(self, k, delt):
        self.add_tag[k] = ring.add(self.add_tag[k], delt)
        self.value[k] = ring.add(self.value[k], ring.mul(self.length(k), delt))
        
    def update_mul(self, k, delt):
        self.add_tag[k] = ring.mul(self.add_tag[k], delt)
        self.mul_tag[k] = ring.mul(self.mul_tag[k], delt)
        self.value[k] = ring.mul(self.value[k], delt)

    def push_up(self, k):
        self.value[k] = ring.add(self.value[ls(k)], self.value[rs(k)])

    def push_down(self, k):
        add_delt = self.add_tag[k]
        mul_delt = self.mul_tag[k]

        self.update_mul(ls(k), mul_delt), self.update_mul(rs(k), mul_delt)
        self.update_add(ls(k), add_delt), self.update_add(rs(k), add_delt)

        self.add_tag[k] = 0
        self.mul_tag[k] = 1

    def build(self, k, l, r):
        self.left[k], self.right[k] = l, r

        if l == r:
            self.value[k] = self.array[l]
        else:
            m = self.m(k)

            self.build(ls(k), l, m)
            self.build(rs(k), m + 1, r)
            self.push_up(k)

    def _modify(self, k, a, b, delt):
        if a <= self.left[k] and self.right[k] <= b:
            self.update(k, delt)
        else:
            self.push_down(k)
            m = self.m(k)

            if a <= m:
                self._modify(ls(k), a, b, delt)
            if b > m:
                self._modify(rs(k), a, b, delt)
            self.push_up(k)

    def _query(self, k, a, b):
        res = 0

        if a <= self.left[k] and self.right[k] <= b:
            return self.value[k]

        self.push_down(k)
        m = self.m(k)

        if a <= m:
            res = ring.add(res, self._query(ls(k), a, b))
        if m < b:
            res = ring.add(res, self._query(rs(k), a, b))

        return res

    def modify(self, a, b, delt):
        self._modify(1, a, b, delt)

    def query(self, a, b):
        return self._query(1, a, b)


if __name__ == '__main__':
    n, m, _ = map(int, input().split())
    array = [int(x) for x in input().split()]

    tree = SegmentTree(array)

    for _ in range(m):
        iter = map(int, input().split())
        cmd, a, b = next(iter), next(iter), next(iter)

        if cmd == 3:
            print(tree.query(a, b))
        else:
            tree.set_update(cmd)
            k = next(iter)

            tree.modify(a, b, k)