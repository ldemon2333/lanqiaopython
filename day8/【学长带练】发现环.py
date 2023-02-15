from sys import setrecursionlimit

setrecursionlimit(int(1e6))


n = int(input())
graph = [set() for _ in range(n + 1)]
done = False

for _ in range(n):
    a, b = map(int, input().split())

    graph[a].add(b)
    graph[b].add(a)


def print_circle(k):
    i = track.index(k)

    print(*sorted(track[i:]))


track = []


def search(i, j):
    track.append(j)
    dfs(i, j)
    track.pop()


def dfs(i, j):
    global done
    
    if done:
        return

    for k in graph[j]:
        if k == i:
            continue

        if k in track:
            print_circle(k)
            done = True
        else:
            search(j, k)


search(0, 1)