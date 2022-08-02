"""Provides the Token class and global variables for categorizing Tokens."""
from enum import Enum, unique
import math

FUNCTIONS = {
    "sin": lambda x: math.sin(x),
    "cos": lambda x: math.cos(x),
    "tan": lambda x: math.tan(x),
}


class TokenType(Enum):
    NUMERIC = 1
    OPERATOR = 2
    DECIMAL = 3
    FUNCTION = 4


@unique
class Operators(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    OPEN_BRACKET = "("
    CLOSE_BRACKET = ")"
    EXPONENTIATE = "^"

    @staticmethod
    def get_operators_list():
        """Returns a list of all the Operator enum values"""
        return [operator.value for operator in list(Operators)]


class Token():
    """Holds the value and type of a token."""

    def __init__(self, value, tokenType):
        self.value = value
        self.tokenType = tokenType

    def __str__(self):
        return "Token({}, {})".format(self.tokenType, self.value)

    def __repr__(self):
        return self.__str__()

    def resolve(self):
        raise Exception()

    @ classmethod
    def createTokenFromChar(cls, value):
        """Conditionally creates token with TokenType pre-populated depending on value"""
        if value.isnumeric():
            return cls(value, TokenType.NUMERIC)
        elif value in Operators.get_operators_list():
            return cls(value, TokenType.OPERATOR)
        elif value == '.':
            return cls(value, TokenType.DECIMAL)


class FunctionalToken(Token):
    """A special token class for scientific functions."""

    def __init__(self, string):
        self.tokenType = TokenType.FUNCTION
        self.value = None
        self._string = string

    def resolve(self):
        """Evaluates the trigonemtric expression and updates the FunctionalToken's value"""
        function_name = ""
        function_input = ""
        for i in range(len(self._string)):
            if self._string[i].isalpha():
                function_name += self._string[i]
            else:
                function_input += self._string[i]
        try:
            self.value = FUNCTIONS[function_name](eval(function_input))
        except KeyError:
            raise Exception(
                f"Could not recognise {function_name} as a valid function")
