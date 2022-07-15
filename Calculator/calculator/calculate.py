from parser import Parser
from tokenizer import Tokenizer
from utils import Stack, calculations


class Calculator():
    def __init__(self):
        self._tokenizer = Tokenizer()
        self._parser = Parser()
        self._calculatorStack = Stack()

    def calculate(self, str):
        tokens = self._tokenizer.tokenize(str)
        parsedTokensQueue = self._parser.parse(tokens)
        print(parsedTokensQueue)

        while parsedTokensQueue:
            token = parsedTokensQueue.popleft()
            if token not in ['*', '+', '-', '/', '^']:
                self._calculatorStack.push(token)
            else:
                result = calculations[token](
                    float(self._calculatorStack.pop()), float(self._calculatorStack.pop()))
                print(result)
                self._calculatorStack.push(result)

        return result
