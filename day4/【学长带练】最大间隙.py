n = int(input())

a = [int(x) for x in input().split()]

delts = [a[i] - a[i - 1] for i in range(1, n)]

print(max(delts))