from collections import deque

class Queue:
    def __init__(self):
        self._q = deque()
    def push(self, x):
        self._q.append(x)
    def pop(self):
        return self._q.popleft() if self._q else None
