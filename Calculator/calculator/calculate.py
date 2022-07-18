from parser import Parser, OPERATORS
from tokenizer import Tokenizer
from utils import Stack
from decimal import *


CALCULATIONS = {
    "+": lambda a, b:  a + b,
    '-': lambda b, a: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b / a,
    '^': lambda a, b: a ** b  # TO BE IMPELEMENTED IN FUTURE
}


class Calculator():
    """Composed with Tokenizer, Parser, and Stack class uses those in conjunction to perform a calculation"""

    def __init__(self):
        self._tokenizer = Tokenizer()
        self._parser = Parser()
        self._calculatorStack = Stack()

    def calculate(self, str):
        """accepts string, converts it into a queue of characters in post fix notation and cacluates the result"""
        tokens = self._tokenizer.tokenize(str)
        parsedTokensQueue = self._parser.parse(tokens)

        # Remove elements from the queue one by one
        while parsedTokensQueue:
            token = parsedTokensQueue.popleft()
            if token not in OPERATORS:
                self._calculatorStack.push(token)
            else:
                result = CALCULATIONS[token](
                    Decimal(self._calculatorStack.pop()), Decimal(self._calculatorStack.pop()))
                self._calculatorStack.push(result)

        return float(result)
