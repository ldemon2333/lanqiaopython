class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def get_mod(self, a):
        return a % self.mod if self.mod else a

    def _add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b

    def add(self, *args):
        s = 0
        for i in args:
            s = self._add(s, i)
        return s

    def sum(self, iterable):
        return self.add(*iterable)

    def mul_(self, a, b):
        return (a * b) % self.mod if self.mod else a * b

    def mul(self, *args):
        res = 1
        for i in args:
            res = self.mul_(res, i)
        return res

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


class LinearSpace(ModCalculation):
    def __init__(self, dim, mod=0):
        super().__init__(mod)
        self.dim = dim

        self.E = [[0] * dim for _ in range(dim)]
        for i in range(dim):
            self.E[i][i] = 1

    def axb(self, a, b):
        return self.sum(self.mul(i, j) for i, j in zip(a, b))

    def axA(self, a, A):
        return [self.sum(self.mul(a[i], A[i][j]) for i in range(self.dim)) for j in range(self.dim)]

    def AxB(self, A, B):
        return [self.axA(a, B) for a in A]

    def quick_power(self, A, n):
        res = self.E

        B = A
        while n:
            if n & 1:
                res = self.AxB(res, B)

            B = self.AxB(B, B)
            n >>= 1

        return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    space = LinearSpace(3, m)

    M = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
    a = [-1, 1, 1]

    A = space.quick_power(M, n)
    print(space.axA(a, A)[0])