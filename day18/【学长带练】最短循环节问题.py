def min_circle(s):
    for size in range(1, len(s) + 1):
        sub = s[: size]

        q, r = divmod(len(s), size)
        n = len(s) - r
        
        if sub[: r] == s[n:]:
            if s.count(sub, 0, n) == q:
                return size


if __name__ == '__main__':
    n = int(input())
    s = input()

    print(min_circle(s))