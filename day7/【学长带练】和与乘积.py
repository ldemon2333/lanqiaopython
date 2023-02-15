def count(left, right, delt):
    min, max = left, right
    if min > max:
        min, max = max, min

    total = left + right

    if delt < 0 or delt > total:
        return 0

    if delt <= min:
        return delt + 1

    if delt >= max:
        return total - delt + 1

    return min + 1


sum = [0]

s = lambda l, r: sum[r] - sum[l - 1]


index = [0]


if __name__ == '__main__':
    n = int(input())
    a = [None] + [int(x) for x in input().split()]

    for i in range(1, n + 1):
        sum.append(sum[-1] + a[i])

        if a[i] > 1:
            index.append(i)

    ans = n

    index.append(n + 1)
    up = len(index) - 1

    for i in range(1, up):
        last_l = index[i - 1]
        l = index[i]

        p = a[l]

        upper = min(up, i + 35)                   # j - i + 1 < 36

        for j in range(i + 1, upper):
            r = index[j]
            r_next = index[j + 1]

            p *= a[r]
            delt = p - s(l, r)

            left = l - last_l - 1
            right = r_next - r - 1

            ans += count(left, right, delt)

    print(ans)