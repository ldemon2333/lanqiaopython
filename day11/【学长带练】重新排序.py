ls = lambda k: 2 * k
rs = lambda k: 2 * k + 1


class SegmentTree:
    def __init__(self, array):  # element index starts from 0
        self.n = len(array)
        self.size = 4 * self.n

        self.array = [0] + array

        self.left, self.right = [0] * self.size, [0] * self.size
        self.value, self.tag = [0] * self.size, [0] * self.size

        self.build(1, 1, self.n)

    def m(self, k):
        return (self.left[k] + self.right[k]) // 2

    def length(self, k):
        return self.right[k] - self.left[k] + 1

    def update(self, k, delt):
        self.tag[k] += delt
        self.value[k] += delt * self.length(k)

    def push_up(self, k):
        self.value[k] = self.value[ls(k)] + self.value[rs(k)]

    def push_down(self, k):
        delt = self.tag[k]
        self.update(ls(k), delt), self.update(rs(k), delt)
        self.tag[k] = 0

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
            res += self._query(ls(k), a, b)
        if m < b:
            res += self._query(rs(k), a, b)

        return res

    def modify(self, a, b, delt):
        self._modify(1, a, b, delt)

    def query(self, a, b):
        return self._query(1, a, b)


def append_sort(list):
    return [0] + sorted(list)


if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in input().split()]

    tree_sum = SegmentTree(A)
    tree_cnt = SegmentTree([0] * n)

    A_query = 0
    A_sorted = append_sort(A)

    for _ in range(int(input())):
        l, r = map(int, input().split())

        A_query += tree_sum.query(l, r)

        tree_cnt.modify(l, r, 1)

    counts = append_sort([tree_cnt.query(i, i) for i in range(1, n + 1)])
    query = sum([a * cnt for a, cnt in zip(A_sorted, counts)])

    print(query - A_query)