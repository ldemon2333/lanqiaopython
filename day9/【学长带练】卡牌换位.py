from collections import deque


def around(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def swap(matrix, x, y, i, j):
    matrix[x][y], matrix[i][j] = matrix[i][j], matrix[x][y]


def next_graph(graph, x, y):
    a, b = graph
    matrix = [list(a), list(b)]

    for i, j in around(x, y):
        if 0 <= i < 2 and 0 <= j < 3:
            swap(matrix, x, y, i, j)
            
            a, b = matrix
            yield tuple(a), tuple(b)
            
            swap(matrix, x, y, i, j)


def locate(graph, s):
    a, b = graph
    
    if s in a:
        return 0, a.index(s)
    return 1, b.index(s)
    

track = set()
q = deque()


def push(graph):
    if graph not in track:
        track.add(graph)
        q.append(graph)


start = tuple(x for x in input()), tuple(x for x in input())
A, B = locate(start, 'B'), locate(start, 'A')


def bfs(graph, step):
    push(graph)
    
    while q:
        step += 1

        for _ in range(len(q)):
            graph = q.popleft()
            
            if locate(graph, 'A') == A and locate(graph, 'B') == B:
                return step

            space = locate(graph, ' ')
            for g in next_graph(graph, *space):
                push(g)

    return step


print(bfs(start, -1))