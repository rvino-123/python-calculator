# Token types go here
NUMERIC = "NUMERIC"
OPERATOR = "OPERATOR"
DECIMAL = "DECIMAL"
OPERATORS = ('*', '/', '-', '+', '(', ')')


class Token():
    """Holds the value and type of a token."""

    def __init__(self, value, tokenType):
        self.value = value
        self.tokenType = tokenType

    def __str__(self):
        return "Token({}, {})".format(self.tokenType, self.value)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def createTokenFromChar(cls, value):
        """conditionally creates token with TokenType pre-populated depending on value"""
        if value.isnumeric():
            return cls(value, NUMERIC)
        elif value in OPERATORS:
            return cls(value, OPERATOR)
        elif value == '.':
            return cls(value, DECIMAL)
