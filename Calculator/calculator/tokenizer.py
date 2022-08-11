from tokentypes import Token, FunctionalToken


def tokenize(str):
    """returns a list of tokens from a string"""
    tokenQueue = []
    # Get rid of all spaces
    text_no_spaces = str.replace(" ", "")
    i = 0
    while True:
        if i == len(text_no_spaces):
            break
        if text_no_spaces[i].isalpha():
            j = i + 1
            while text_no_spaces[j] != ")":
                j += 1
            func_token = FunctionalToken(text_no_spaces[i:j+1])
            # Ensures the functional token resolves it's value before entering the queue.
            func_token.resolve()
            tokenQueue.append(func_token)
            # Propogates the loop past the extracted functional token.
            i = j + 1
            continue
        token = Token.createTokenFromChar(text_no_spaces[i])
        tokenQueue.append(token)
        i += 1
    return tokenQueue
