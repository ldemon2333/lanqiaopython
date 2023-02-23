def max_fix(s):
    max_same = [0] * len(s)

    for i in range(1, len(s)):
        j = i - 1

        while j >= 0:
            pi = max_same[j]

            if s[i] == s[pi]:
                max_same[i] = pi + 1
                break

            j = pi - 1

    return max_same


def min_fix(s):
    min_same = max_fix(s)

    for i in range(1, len(s)):
        j = i                       # initial j as i > 0

        while pi := min_same[j]:    # ensure j and pi > 0
            min_same[i] = pi
            j = pi - 1              # worst j is 0

    return min_same


if __name__ == '__main__':
    n = int(input())
    s = input()

    min_same = min_fix(s)

    cnt = 0
    for i in range(1, n):
        if same := min_same[i]:
            size = i + 1

            if same <= size // 2:
                cnt += size - same

    print(cnt)