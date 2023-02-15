def search(n):
    m = int(n ** 0.5)

    dic = {}
    
    for i in range(m + 1):
        a = i * i
        for j in range(i, m + 1):
            b = a + j * j

            if b > n:
                break

            if b not in dic:
                dic[b] = i, j

    for i in range(m + 1):
        a = i * i
        for j in range(i, m + 1):
            b = a + j * j
            
            if b > n:
                break

            c = n - b
            if c in dic:
                return (i, j) + dic[c]


if __name__ == '__main__':
    print(*search(int(input())))