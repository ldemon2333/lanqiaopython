class Window:
    from collections import deque

    def __init__(self):
        self.queue = self.deque()

        self.sum = 0

    def __len__(self):
        return len(self.queue)

    def push(self, x):
        self.queue.append(x)

        self.sum += x

    def pop(self):
        self.sum -= self.queue.popleft()

    def true(self, target):
        return self.sum >= target


class Solution:
    def minSubArrayLen(self, target, nums):
        window = Window()

        m = float('inf')

        for i in nums:
            window.push(i)
            
            while window.true(target):
                m = min(m, len(window))
                
                window.pop()

        return m if m < float('inf') else 0