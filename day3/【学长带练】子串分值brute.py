class Counter:
    def __init__(self, s):
        self.record = {}

        for c in s:
            self.add(c)
    
    def add(self, c):
        if c in self.record:
            self.record[c] = False
        else:
            self.record[c] = True

    def count(self):
        l = list(self.record.values())
        return l.count(True)


if __name__ == '__main__':
    s = input()
    n = len(s)

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            counter = Counter(s[i: j])

            cnt += counter.count()
    print(cnt)