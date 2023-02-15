class MonotonicQueue:
    from collections import deque

    def __init__(self, type, sub=[]):
        self.type = type == 'decrease'

        self.queue = self.deque()

        for i in sub:
            self.push(i)

    def head(self):
        return self.queue[0]

    def is_monotonic(self, x):
        tail = self.queue[-1]

        return tail >= x if self.type else tail <= x

    def push(self, x):
        while self.queue and not self.is_monotonic(x):
            self.queue.pop()

        self.queue.append(x)

    def pop(self, value):
        if self.head() == value:
            self.queue.popleft()


def clockwise_reshape(list, index, reverse=False):
    step = -1 if reverse else 1

    return list[index:: step] + list[: index: step]


def min_delt(P, D):
    delts = []

    n = len(P)
    P_double, D_double = P * 2, D * 2

    for i in range(1, n * 2):
        P_double[i] += P_double[i - 1]
        D_double[i] += D_double[i - 1]

    fuel = [p - d for p, d in zip(P_double, D_double)]

    min_queue = MonotonicQueue('increase', fuel[: n])
    delts.append(min_queue.head())

    for old_left in range(n - 1):
        new_right = old_left + n

        min_queue.pop(fuel[old_left])
        min_queue.push(fuel[new_right])

        delts.append(min_queue.head() - fuel[old_left])

    return delts


if __name__ == '__main__':
    n = int(input())

    P, D = [], []
    for _ in range(n):
        p, d = map(int, input().split())

        P.append(p), D.append(d)

    delts = min_delt(P, D)

    P_rev = clockwise_reshape(P, -1, True)
    D_rev = clockwise_reshape(D, -2, True)

    delts_rev = min_delt(P_rev, D_rev)
    delts_rev = clockwise_reshape(delts_rev, -1, True)

    for i, j in zip(delts, delts_rev):
        if max(i, j) < 0:
            print('NIE')
        else:
            print('TAK')