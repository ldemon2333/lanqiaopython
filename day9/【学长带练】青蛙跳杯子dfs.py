from sys import setrecursionlimit

setrecursionlimit(int(1e5))


a, b = input(), input()
n = len(a)


def next_str(s, i, j):
    l = list(s)
    l[i], l[j] = l[j], l[i]
    return ''.join(l)


m = float('inf')
track = set()


def search(s, step):
    if s not in track:
        track.add(s)
        dfs(s, step)
        track.remove(s)


def dfs(s, step):
    global m

    if step >= m:
        return

    if s == b:
        m = step
        return

    k = s.find('*')

    for i in range(k - 3, k + 4):
        if 0 <= i < n:
            si = next_str(s, k, i)
            
            search(si, step + 1)


search(a, 0)
print(m)