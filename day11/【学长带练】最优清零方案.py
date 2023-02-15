get_line = lambda: map(int, input().split())

n, k = get_line()
array = list(get_line())

def find_min(l):
  min = float('inf')
  index = -1

  for i in range(l, l + k):
    if array[i] <= min:
      min = array[i]
      index = i

  return min, index

cnt = 0
l = 0
while l + k <= n:       # r = l + k - 1 <= n - 1
    min, index = find_min(l)

    cnt += min

    for i in range(l, l + k):
       array[i] -= min

    l = index + 1

cnt += sum(array)
print(cnt)