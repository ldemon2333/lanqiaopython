def clockwise_reshape(list, index, reverse=False):
    step = -1 if reverse else 1

    return list[index:: step] + list[: index: step]


def min_delt(P, D):
    res = []

    n = len(P)
    P_double, D_double = P * 2, D * 2

    for l in range(n):
        P_sub = P_double[l: l + n]
        D_sub = D_double[l: l + n]

        for i in range(1, n):
            P_sub[i] += P_sub[i - 1]
            D_sub[i] += D_sub[i - 1]

        delts = [p - d for p, d in zip(P_sub, D_sub)]
        res.append(min(delts))

    return res


if __name__ == '__main__':
    n = int(input())

    P, D = [], []
    for _ in range(n):
        p, d = map(int, input().split())

        P.append(p), D.append(d)

    delts = min_delt(P, D)

    P_rev = clockwise_reshape(P, -1, True)
    D_rev = clockwise_reshape(D, -2, True)

    delts_rev = min_delt(P_rev, D_rev)
    delts_rev = clockwise_reshape(delts_rev, -1, True)

    for i, j in zip(delts, delts_rev):
        if max(i, j) < 0:
            print('NIE')
        else:
            print('TAK')