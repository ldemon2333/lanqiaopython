def num_to_int(s):
    try:
        return int(s)
    except:
        return s


class Record:
    def __init__(self):
        self.dict = {}

    def add(self, key, i, j):
        if key not in self.dict:
            self.dict[key] = set()

        self.dict[key].add(i)
        self.dict[key].add(j)

    def max(self):
        try:
            return max([len(v) for v in self.dict.values()])
        except:
            return 1


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
            else:
                if dv > 0:
                    time += dist / dv
                    coordinate += v * time

                    record.add((time, coordinate), i, j)

    return record.max()


X, Y = [], []


if __name__ == '__main__':
    for _ in range(int(input())):
        x, y, v, d = map(num_to_int, input().split())

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