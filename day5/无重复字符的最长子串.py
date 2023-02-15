class Window:
    from collections import deque

    def __init__(self):
        self.queue = self.deque()

    def __len__(self):
        return len(self.queue)

    def push(self, x):
        self.queue.append(x)
        
    def pop(self):
        self.queue.popleft()
        
    def true(self):
        q_set = set(self.queue)

        return len(self) == len(q_set)


class Solution:
    def lengthOfLongestSubstring(self, s):
        window = Window()

        M = 0

        for i in s:
            window.push(i)

            while not window.true():
                window.pop()

            M = max(M, len(window))

        return M