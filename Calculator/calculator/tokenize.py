import tokentypes
from utils import Queue


class Tokenizer():
    """Parses the command string and returns a queue with tokens"""
    @staticmethod
    def tokenize(str):
        """returns a queue of tokens from a string"""
        tokenQueue = Queue()
        # Get rid of all spaces
        text_no_spaces = str.replace(" ", "")
        for c in text_no_spaces:
            token = tokentypes.Token.createTokenFromChar(c)
            tokenQueue.enqueue(token)
        return tokenQueue
