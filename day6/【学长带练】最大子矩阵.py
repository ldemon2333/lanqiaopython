class MonotonicQueue:
    from collections import deque

    def __init__(self, type_):
        self.queue = self.deque()
        self.max = type_ == 'max'

    def value(self):
        return self.queue[0]

    def pop(self, x):
        if self.value() == x:
            self.queue.popleft()

    def not_value(self, x):
        return self.queue[-1] >= x if self.max else self.queue[-1] <= x

    def push(self, x):
        while self.queue:

            if self.not_value(x):
                break

            self.queue.pop()

        self.queue.append(x)


class Pair:
    def __init__(self):
        self.max_queue = MonotonicQueue('max')
        self.min_queue = MonotonicQueue('min')

    def pop(self, x):
        self.max_queue.pop(x)
        self.min_queue.pop(x)

    def push(self, x):
        self.max_queue.push(x)
        self.min_queue.push(x)

    def max(self):
        return self.max_queue.value()

    def min(self):
        return self.min_queue.value()


class Window:
    def __init__(self, matrix, limit, up, down):
        self.matrix = matrix
        self.limit = limit
        self.up = up
        self.down = down
        self.width = down - up + 1
        self.queues_list = [Pair() for _ in range(self.width)]

        self.length = 0

    def size(self):
        return self.length * self.width

    def pop(self, k):
        self.length -= 1

        for i in range(self.width):
            self.queues_list[i].pop(self.matrix[i + self.up][k])

    def push(self, k):
        self.length += 1

        for i in range(self.width):
            self.queues_list[i].push(self.matrix[i + self.up][k])

    def not_stable(self):
        if self.length == 0:
            return False

        max_list = [pair.max() for pair in self.queues_list]
        min_list = [pair.min() for pair in self.queues_list]

        return max(max_list) - min(min_list) > self.limit


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    limit = int(input())
    
    M = 0
    for i in range(n):
        for j in range(i, n):
            window = Window(matrix, limit, i, j)

            for k in range(m):
                window.push(k)

                while window.not_stable():
                    window.pop(k - window.length + 1)

                M = max(M, window.size())
    print(M)