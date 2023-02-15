class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b

    def sum(self, iterable):
        s = 0
        for i in iterable:
            s = self.add(s, i)
        return s

    def mul(self, a, b):
        return (a * b) % self.mod if self.mod else a * b


ring = ModCalculation(int(1e9) + 7)
n = int(input())

one, two = [0] * (n + 1), [0] * (n + 1)

one[2] = 2
two[1] = 1
two[2] = 2

for i in range(3, n + 1):
    one[i] = ring.add(one[i - 1], ring.mul(2, two[i - 2]))
    two[i] = ring.sum((one[i - 1], two[i - 1], two[i - 2]))

print(two[n])