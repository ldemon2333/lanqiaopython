from math import ceil


def is_prefix(s, sub):
    return s[: len(sub)] == sub


def max_circle(s):
    tail = len(s) - 1
    middle = ceil(len(s) / 2) - 1

    for size in range(tail, middle, -1):
        pre, suf = s[: size], s[size:]

        if is_prefix(pre, suf):
            return size

    return 0


if __name__ == '__main__':
    n = int(input())
    s = input()

    cnt = 0
    for i in range(2, n + 1):
        cnt += max_circle(s[: i])
    print(cnt)