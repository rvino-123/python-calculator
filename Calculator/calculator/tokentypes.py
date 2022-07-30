"""Provies the Token class and global variables for categorizing Tokens."""
from enum import Enum

# Token types go here


class TokenType(Enum):
    NUMERIC = 1
    OPERATOR = 2
    DECIMAL = 3


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
            return cls(value, TokenType.NUMERIC)
        elif value in OPERATORS:
            return cls(value, TokenType.OPERATOR)
        elif value == '.':
            return cls(value, TokenType.DECIMAL)
