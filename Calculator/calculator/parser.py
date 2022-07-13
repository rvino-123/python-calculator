from utils import Stack

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


class Parser():
    """Holds and returns the numerical and operator stacks after populating them"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = Stack()
        self.currentTokenType = None

    def parse(self):
        """Iterates through the tokens and allocates token to revelant stack"""
        pass

    def getStack(self):
        return self.stack
