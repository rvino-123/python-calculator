from collections import deque


class Stack:
    """Own implementation of Stack DataStructure"""

    def __init__(self):
        self._container = deque()

    def push(self, value):
        """Adds an Element to the Stack"""
        self._container.append(value)

    def pop(self):
        """Removes and returns the most recently added element from the Stack."""
        return self._container.pop()

    def peek(self):
        """Returns but DOES NOT REMOVE the most recently added element from the Stack."""
        return self._container[-1]

    def printWholeStack(self):
        return self._container

    def __len__(self):
        return len(self._container)
