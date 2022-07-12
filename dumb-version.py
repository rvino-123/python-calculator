from collections import deque
from utils.stack import Stack

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

# dictionary having priorities of Operator
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

calculations = {
    "+": lambda a, b:  a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ^ b
}


string1 = "3 - 2 + 1"
string2 = " 32 * (2 + 5) * (10 + 5) "
tokenArray = []

operatorStack = Stack()
numericalStack = Stack()


class Token():
    def __init__(self, value, tokenType):
        self.value = value
        self.tokenType = tokenType

    def __str__(self):
        return "Token({}, {})".format(self.tokenType, self.value)
    # Helps identify the tokens being created

    def __repr__(self):
        return self.__str__()

    @classmethod
    def createTokenFromChar(cls, value):
        if value.isnumeric():
            return cls(value, 'NUMERIC')
        elif value in ['*', '/', '-', '+', '(', ')']:
            return cls(value, 'OPERATOR')


string2_no_spaces = string2.replace(" ", '')

for char in string2_no_spaces:
    token = Token.createTokenFromChar(char)
    tokenArray.append(token)


def tokenize(commandString):
    string2_no_spaces = commandString.replace(" ", '')
    currentChar = ""

    tokens = []
    print(string2_no_spaces)
    for char in string2_no_spaces:
        token = Token.createTokenFromChar(char)
        tokens.append(token)
    return tokens


def parse(tokens):
    parseStack = Stack()
    parseQueue = deque()
    intBuffer = ""

    for token in tokens:
        currentTokenType = token.tokenType
        currentTokenValue = token.value
        # print(currentTokenValue)
        if currentTokenValue not in Operators:
            if currentTokenType == "NUMERIC":
                intBuffer += currentTokenValue
                # print("int buffer: ", intBuffer)
        elif currentTokenValue == "(":
            parseStack.push(currentTokenValue)
        elif currentTokenValue == ")":
            parseQueue.append(intBuffer)
            intBuffer = ""
            while parseStack and parseStack.peek() != "(":
                parseQueue.append(parseStack.pop())
            parseStack.pop()
        else:
            if intBuffer != "":
                parseQueue.append(intBuffer)
                intBuffer = ""
            while parseStack and parseStack.peek() != '(' and Priority[currentTokenValue] <= Priority[parseStack.peek()]:
                parseQueue.append(parseStack.pop())
            parseStack.push(currentTokenValue)
            # print(parseStack.printWholeStack())
    while parseStack:
        if intBuffer != "":
            parseQueue.append(intBuffer)
            intBuffer = ""
        parseQueue.append(parseStack.pop())
    return parseQueue


def calculate(calculateQueue):
    # reading from left to right, push element in stack
    calculateStack = Stack()
    for i in range(len(calculateQueue)):
        char = calculateQueue[i]
        print(char)
        if char not in Operators:
            calculateStack.push(char)
        else:
            result = calculations[char](
                int(calculateStack.pop()), int(calculateStack.pop()))
            if i < len(calculateQueue):
                calculateStack.push(result)
        print(calculateStack.printWholeStack())
    return result

    # if it is an operand, add it to the stack
    # if it is an operator, pop two operands from the stack and evaluate
    # push the evaluation result back into the stack


my_tokens = tokenize(string2)
print(my_tokens)
parsedTokens = parse(my_tokens)
print(calculate(parsedTokens))
