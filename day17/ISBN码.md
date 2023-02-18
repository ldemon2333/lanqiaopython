## 题目大意

判断ISBN码是否合法

## 解题思路

ISBN码的识别码为其前9位数字的和，每位数字乘以其所在位置的权重，权重从1开始，权重和对11取模，如果余数为10，则识别码为X，否则为余数。
只要判断识别码是否与输入的最后一位相同即可。

## AC_Code

Python程序：

```python
isbn = input()
l = [x for x in isbn if x != '-']

n = sum([i * int(l[i - 1]) for i in range(1, 10)]) % 11
r = 'X' if n == 10 else str(n)

print('Right' if r == l[-1] else isbn[: -1] + str(r))
```