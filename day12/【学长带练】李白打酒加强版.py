class Cache:
    def __init__(self):
        from sys import setrecursionlimit
        from functools import lru_cache

        setrecursionlimit(int(1e6))

        self.lru_cache = lru_cache

    def func(self):
        return self.lru_cache(maxsize=None)     # return key is function


class ModCalculation:
    def __init__(self, mod=0):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod if self.mod else a + b


cache = Cache()
ring = ModCalculation(int(1e9) + 7)


@cache.func()
def count(div, plus, s):
    if plus == 0 and div == 0:
        return 1 if s == 2 else 0

    cnt = 0
    
    if plus:
        cnt = ring.add(cnt, count(div, plus - 1, s + 1))
    
    if div and s % 2 == 0:
        cnt = ring.add(cnt, count(div - 1, plus, s // 2))
        
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(count(n, m - 1, 1))
