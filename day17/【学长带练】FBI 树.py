_ = input()
s = input()

n = len(s)
N = 4 * n

tree = [''] * N
s = ' ' + s


ls = lambda k: k * 2
rs = lambda k: k * 2 + 1


def push_up(k):
    if tree[ls(k)] == 'B' and tree[rs(k)] == 'B':
        tree[k] = 'B'
    elif tree[ls(k)] == 'I' and tree[rs(k)] == 'I':
        tree[k] = 'I'
    else:
        tree[k] = 'F'


def build(k, l, r):
    if l == r:
        if s[l] == '0':
            tree[k] = 'B'
        else:
            tree[k] = 'I'
    else:
        m = (l + r) // 2

        build(ls(k), l, m)
        build(rs(k), m + 1, r)

        push_up(k)


def dfs(k):
    if tree[k]:
        dfs(ls(k))
        dfs(rs(k))
        print(tree[k], end='')


if __name__ == '__main__':
    build(1, 1, n)
    dfs(1)