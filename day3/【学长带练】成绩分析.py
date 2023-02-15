n = int(input())
l = [int(input()) for _ in range(n)]

avg = sum(l) / n

print(max(l))
print(min(l))

print(f'{avg:.2f}')