class Cache:
    def __init__(self):
        from sys import setrecursionlimit
        from functools import lru_cache

        setrecursionlimit(int(1e6))

        self.lru_cache = lru_cache

    def func(self):
        return self.lru_cache(maxsize=None)     # return key is function


cache = Cache()
choices = [int(x) for x in input().split()]


@cache.func()
def best_result(n, first, after):
    if n == 0:
        if first ^ after:                       # 一真一假可分胜负
            return '+' if first else '-'
        return '0'
    
    best = '-'
    for x in choices:
        if x <= n:
            new_n = n - x
            new_first = after
            new_after = first ^ (x % 2)         # 一奇加一偶方为奇

            enemy_best = best_result(new_n, new_first, new_after)

            if enemy_best == '-':
                return '+'

            if enemy_best == '0':
                best = '0'

    return best


if __name__ == '__main__':                      
    nums = map(int, input().split())            # 初始值零非奇数
    print(*[best_result(n, False, False) for n in nums])