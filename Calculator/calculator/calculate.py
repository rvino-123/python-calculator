from parser import Parser
from tokenizer import Tokenizer
from utils import Stack
from decimal import *

CALCULATIONS = {
    "+": lambda a, b:  a + b,
    '-': lambda b, a: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b / a,
    '^': lambda a, b: b ^ a
}


class Calculator():
    def __init__(self):
        self._tokenizer = Tokenizer()
        self._parser = Parser()
        self._calculatorStack = Stack()

    def calculate(self, str):
        tokens = self._tokenizer.tokenize(str)
        parsedTokensQueue = self._parser.parse(tokens)

        while parsedTokensQueue:
            token = parsedTokensQueue.popleft()
            if token not in ['*', '+', '-', '/', '^']:
                self._calculatorStack.push(token)
            else:
                result = CALCULATIONS[token](
                    Decimal(self._calculatorStack.pop()), Decimal(self._calculatorStack.pop()))
                self._calculatorStack.push(result)

        return float(result)
