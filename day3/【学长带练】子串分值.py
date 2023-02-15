s = ' ' + input()
n = len(s) - 1

index = {}

for i in range(1, n + 1):
    c = s[i]

    if c not in index:
        index[c] = [0]
    
    index[c].append(i)


cnt = 0
for value in index.values():
    value.append(n + 1)
    
    for i in range(1, len(value) - 1):
        cnt += (value[i] - value[i - 1]) * (value[i + 1] - value[i])

print(cnt)