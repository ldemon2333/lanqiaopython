class Cache:
    def __init__(self):
        from sys import setrecursionlimit
        from functools import lru_cache

        setrecursionlimit(int(1e6))

        self.lru_cache = lru_cache

    def func(self):
        return self.lru_cache(maxsize=None)     # return key is function


cache = Cache()

win = ['*OL', 'L*L', 'LO*']


def situayions(s):
    for i in range(len(s)):
        a = s[: i]
        b = s[i + 1:]

        if s[i] == '*':
            yield a + 'L' + b
            yield a + 'O' + b


def solve(s):                       # 不同初始情况重新缓存

    @cache.func()
    def best_result(s):             # 默认初始情况不是赢局/平局/输局
        if any(w in s for w in win):
            return 1

        if s.count('*') == 1:
            return 0

        best = -1
        for si in situayions(s):
            enemy_best = best_result(si)

            if enemy_best == -1:
                return 1            # 剪枝

            if enemy_best == 0:
                best = 0

        return best

    print(best_result(s))


if __name__ == '__main__':
    for _ in range(int(input())):
        solve(input())