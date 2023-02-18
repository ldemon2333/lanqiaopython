def str_xor(a, b):
    s = ''
    for i, j in zip(a, b):
        s += str(int(i) ^ int(j))
    return s


if __name__ == '__main__':
    n = int(input())
    s = input()

    xor_value = str_xor(s, s[:: -1])
    print(len(xor_value.split('0')))