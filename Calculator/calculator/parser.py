import tokentypes
from utils import Stack
from collections import deque

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
Operators = set(['+', '-', '*', '/', '(', ')', '^'])


class Parser():
    """Holds and returns the numerical and operator stacks after populating them"""

    @staticmethod
    def parse(tokens):
        """Iterates through the tokens and returns a queue in postfix notation format"""
        parseStack = Stack()
        parseQueue = deque()
        intBuffer = ""  # to combine multiple numeric tokens for multi-digit numbers

        for token in tokens:
            currentTokenType = token.tokenType
            currentTokenValue = token.value

            if currentTokenValue not in Operators:
                if currentTokenType == tokentypes.NUMERIC:
                    intBuffer += currentTokenValue

            elif currentTokenValue == "(":
                parseStack.push(currentTokenValue)

            elif currentTokenValue == ")":
                parseQueue.append(intBuffer)
                intBuffer = ""

                while parseStack and parseStack.peek() != "(":
                    parseQueue.append(parseStack.pop())
                parseStack.pop()

            # if current token is an operator not a paranthesis
            else:
                if intBuffer != "":
                    parseQueue.append(intBuffer)
                    intBuffer = ""

                while parseStack and parseStack.peek() != '(' and Priority[currentTokenValue] <= Priority[parseStack.peek()]:
                    parseQueue.append(parseStack.pop())
                parseStack.push(currentTokenValue)

        # empties any remaining numbers and operators
        if intBuffer != "":
            parseQueue.append(intBuffer)
            intBuffer = ""

        while parseStack:
            parseQueue.append(parseStack.pop())
        return parseQueue
