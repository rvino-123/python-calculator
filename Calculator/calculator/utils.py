from collections import deque


class Stack:
    def __init__(self):
        self._container = deque()

    def push(self, value):
        self._container.append(value)

    def pop(self):
        return self._container.pop()

    def peek(self):
        return self._container[-1]

    def printWholeStack(self):
        return self._container

    def __len__(self):
        return len(self._container)
