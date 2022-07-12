import types


class Tokenizer():
    """Parses the command string and returns an array of tokens"""

    def __init__(self):
        self.tokens = []

    def tokenize(self):
        pass

    def getTokens(self):
        return self.tokens


def tokenize(commandString):
    string2_no_spaces = commandString.replace(" ", '')

    tokens = []
    for char in string2_no_spaces.split():
        token = Token(char)
        tokens.append(token)
    tokens.append(Token(""))

    return tokens
