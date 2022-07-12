"""Reads the array of token received from tokenizer and populates relevant Stack structure depending on token type"""
from webbrowser import get
from utils.stack import Stack
# create numerical and operator stack
# adds th


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
