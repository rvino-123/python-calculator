import tokentypes


class Tokenizer():
    """Parses the command string and returns a queue with tokens"""
    @staticmethod
    def tokenize(str):
        """returns a list of tokens from a string"""
        tokenQueue = []
        # Get rid of all spaces
        text_no_spaces = str.replace(" ", "")
        # Instantiates tokens using Token class method
        for c in text_no_spaces:
            token = tokentypes.Token.createTokenFromChar(c)
            tokenQueue.append(token)
        return tokenQueue
