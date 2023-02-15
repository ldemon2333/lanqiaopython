class Record:
    def __init__(self):
        self.dict = {}

    def add(self, key, i, j):
        if key not in self.dict:
            self.dict[key] = set()

        self.dict[key].add(i)
        self.dict[key].add(j)

    def max(self):
        cnts = [len(v) for v in self.dict.values()]

        return max(cnts) if cnts else 1


def max_enemy(dim):
    record = Record()
    dims = len(dim)

    for i in range(dims - 1):
        p, v = dim[i]

        for j in range(i + 1, dims):
            q, w = dim[j]

            dist = q - p
            dv = v - w

            time = 0.0
            coordinate = p

            if dist == 0:
                record.add((time, coordinate), i, j)    
# 若两点出发点速度均相同，两点任意时刻位置相交
# 其中不与第三点相交的时刻位置上只有两点，不多于出发点上点数
# 所以出发点相同时只需要在出发时刻记录一次
            else:
                if dv > 0:
                    time += dist / dv
                    coordinate += v * time

                    record.add((time, coordinate), i, j)

    return record.max()


if __name__ == '__main__':
    X, Y = [], []

    for _ in range(int(input())):
        x, y, v, d = input().split()
        x, y, v = int(x), int(y), int(v)

        if d in 'RL':
            vx, vy = v, 0
        else:
            vx, vy = 0, v

        if d in 'LD':
            vx, vy = -vx, -vy

        X.append((x, vx))
        Y.append((y, vy))

    X.sort()
    Y.sort()

    print(max(max_enemy(X), max_enemy(Y)))