class PrefixArea:
    def __init__(self, matrix):  # matrix extend 0
        n = len(matrix)
        m = len(matrix[0])

        self.area = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                self.area[i][j] = matrix[i][j] + self.two_area(i - 1, j - 1, i, j)

    def two_area(self, x1, y1, x2, y2):  # x1 <= x2, y1 <= y2
        return self.area[x1][y2] + self.area[x2][y1] - self.area[x1][y1]

    def query(self, x1, y1, x2, y2):
        return self.area[x2][y2] - self.two_area(x1 - 1, y1 - 1, x2, y2)


class WindowCounter:
    def __init__(self, left, matrix, up, down):
        self.left = left
        self.right = left - 1

        self.matrix = matrix

        self.up = up
        self.down = down

    def __len__(self):
        return self.right - self.left + 1

    def push(self):
        self.right += 1

    def pop(self):
        self.left += 1

    def true(self, prefix_area, limit):
        sum = prefix_area.query(self.up, self.left, self.down, self.right)
        return sum <= limit


def extend0_matrix_input(n, m):
    return [[0] * (m + 1)] + [[0] + [int(x) for x in input().split()] for _ in range(n)]


if __name__ == '__main__':
    n, m, limit = map(int, input().split())
    matrix = extend0_matrix_input(n, m)

    prefix_area = PrefixArea(matrix)
    cnt = 0

    for up in range(1, n + 1):
        for down in range(up, n + 1):  # left initial 1
            window_counter = WindowCounter(1, matrix, up, down)

            for _ in range(m):
                window_counter.push()

                while not window_counter.true(prefix_area, limit):
                    window_counter.pop()

                cnt += len(window_counter)

    print(cnt)