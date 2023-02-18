def solution():
    secret = input()
    ans = input()

    dic = {}

    def add(key, value):
        if key not in dic:
            dic[key] = value
            return True

    for key, value in zip(secret, ans):
        if not add(key, value):
            return 'Failed'

        if len(dic) == 26:
            break

    if len(dic) < 26 or len(set(dic.values())) < 26:
        return 'Failed'

    s = ''
    for x in input():
        s += dic[x]
    return s


if __name__ == '__main__':
    print(solution())