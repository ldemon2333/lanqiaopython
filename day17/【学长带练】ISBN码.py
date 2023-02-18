isbn = input()
l = [x for x in isbn if x != '-']

n = sum([i * int(l[i - 1]) for i in range(1, 10)]) % 11
r = 'X' if n == 10 else str(n)

print('Right' if r == l[-1] else isbn[: -1] + str(r))