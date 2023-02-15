from collections import deque


a, b = input(), input()
n = len(a)


def next_str(s, i, j):
    l = list(s)
    l[i], l[j] = l[j], l[i]
    return ''.join(l)


track = set()
q = deque() 


def push(s):
    if s not in track:
        track.add(s)
        q.append(s)


def bfs(s, step):
    push(s)
    
    while q:
        step += 1

        for _ in range(len(q)):
            s = q.popleft()

            if s == b:
                return step

            k = s.find('*')
            for i in range(k - 3, k + 4):
                if 0 <= i < n:
                    si = next_str(s, k, i)
                    
                    push(si)

    return step


print(bfs(a, -1))