from parser import Parser
from tokenizer import tokenize
from tokentypes import Operators
from utils import Stack
from decimal import *


CALCULATIONS = {
    "+": lambda a, b:  a + b,
    '-': lambda b, a: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b / a,
    '^': lambda a, b: b ** a
}


class Calculator():
    """Composed with Tokenizer, Parser, and Stack class uses those in conjunction to perform a calculation"""

    def __init__(self):
        self._parser = Parser()
        self._calculatorStack = Stack()

    def calculate(self, str):
        """Accepts string, converts it into a queue of characters in post fix notation and cacluates the result"""
        tokens = tokenize(str)
        parsedTokensQueue = self._parser.parse(tokens)

        if len(parsedTokensQueue) == 1 and parsedTokensQueue[0] not in Operators.get_operators_list():
            return float(parsedTokensQueue.popleft())

        # Remove elements from the queue one by one
        while parsedTokensQueue:
            token = parsedTokensQueue.popleft()
            if token not in Operators.get_operators_list():
                self._calculatorStack.push(token)
            else:
                result = CALCULATIONS[token](
                    Decimal(self._calculatorStack.pop()), Decimal(self._calculatorStack.pop()))
                self._calculatorStack.push(result)

        return float(result)
