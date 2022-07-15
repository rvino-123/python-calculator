from parser import Parser
from tokenizer import Tokenizer
from utils import Stack

CALCULATIONS = {
    "+": lambda a, b:  a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b / a,
    '^': lambda a, b: a ^ b
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
                    float(self._calculatorStack.pop()), float(self._calculatorStack.pop()))
                self._calculatorStack.push(result)

        return result
