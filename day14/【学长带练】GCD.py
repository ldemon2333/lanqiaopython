from math import ceil

a, b = map(int, input().split())
delt = b - a

q = 2 if a > delt else 1
q = max(q, ceil(a / delt))

print(delt * q - a)