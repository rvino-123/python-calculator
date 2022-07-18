import tokentypes
from utils import Stack
from collections import deque

OPERATOR_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}
OPERATORS = set(['+', '-', '*', '/', '(', ')'])


class Parser():
    """Holds and returns the numerical and operator stacks after populating them"""
    @staticmethod
    def parse(tokens):
        """Iterates through the tokens and returns a queue in postfix notation format"""
        parseStack = Stack()
        parseQueue = deque()
        intBuffer = ""  # to combine multiple numeric tokens for multi-digit numbers
        lastTokenType = None

        # loop through tokens and record token type and value
        for token in tokens:
            currentTokenType = token.tokenType
            currentTokenValue = token.value

            # In case decimal is found
            if currentTokenType == tokentypes.DECIMAL:
                intBuffer += currentTokenValue

            # If first token is negative, ensures it will form a negative integer
            if lastTokenType == None and currentTokenValue == '-':
                intBuffer += currentTokenValue
                lastTokenType = currentTokenType
                continue

            # In the case there are negative integers in the middle of the token queue
            if currentTokenType == lastTokenType and currentTokenValue == '-':
                intBuffer += currentTokenValue
                lastTokenType = currentTokenType
                continue

            # For building multiple digit values
            if currentTokenValue not in OPERATORS:
                if currentTokenType == tokentypes.NUMERIC:
                    intBuffer += currentTokenValue

            # To deal with paranthesese
            elif currentTokenValue == "(":
                parseStack.push(currentTokenValue)

            # Closing paranthesis means all operators between the opening and closing are added to the queue
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

                # ensures operator precedence by adding multiply/divide operators before add/subtract
                while parseStack and parseStack.peek() != '(' and OPERATOR_PRIORITY[currentTokenValue] <= OPERATOR_PRIORITY[parseStack.peek()]:
                    parseQueue.append(parseStack.pop())
                parseStack.push(currentTokenValue)
            lastTokenType = currentTokenType

        # empties any remaining numbers and operators prior to returning the queue
        if intBuffer != "":
            parseQueue.append(intBuffer)
            intBuffer = ""

        while parseStack:
            parseQueue.append(parseStack.pop())
        return parseQueue
