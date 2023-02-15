n = int(input())    # 接收参数
a = [int(x) for x in input().split()]

"""计算公式"""
f = lambda i, j: abs(i - j) + abs(a[i] - a[j])


ans = 0     # 双重循环更新最大值

for i in range(n - 1):
    for j in range(i + 1, n):
        ans = max(ans, f(i, j))

print(ans)