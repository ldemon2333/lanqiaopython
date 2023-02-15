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


class AdjMatrix:
    def __init__(self, vertex_num, max_dist):       # vertex_num from 0 to vertex_num - 1
        self.vertex_num = vertex_num
        self.max_dist = max_dist

        self.size = vertex_num * max_dist
        self.matrix = [[0] * self.size for _ in range(self.size)]

        for i in range(vertex_num):
            for j in range(1, max_dist):
                front = self.get_vertex(i, j - 1)
                back = self.get_vertex(i, j)

                self.matrix[front][back] = 1

    def get_vertex(self, i, j):
        return i * self.max_dist + j

    def add_edge(self, a, b, w):
        if w:
            front = self.get_vertex(a, w - 1)
            back = self.get_vertex(b, 0)

            self.matrix[front][back] = 1

    def calc_graph(self, steps, mod=0):
        space = LinearSpace(self.size, mod)

        self.matrix = space.quick_power(self.matrix, steps)

    def calc_path(self, a, b):
        front = self.get_vertex(a, 0)
        back = self.get_vertex(b, 0)

        return self.matrix[front][back]


if __name__ == '__main__':
    n, steps = map(int, input().split())
    graph = AdjMatrix(n, 9)

    for i in range(n):
        dist = [int(x) for x in input()]

        for j in range(n):
            graph.add_edge(i, j, dist[j])

    graph.calc_graph(steps, 2009)
    print(graph.calc_path(0, n - 1))