Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

# dictionary having priorities of Operators
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infixToPostfix(expression):

    stack = []  # initialization of empty stack

    output = ''

    for character in expression:
        # print(f"character: {character}")
        if character not in Operators:  # if an operand append in postfix expression

            output += character
            # print('output: ', output)

        elif character == '(':  # else Operators push onto stack

            stack.append('(')
            # print("found (")

        elif character == ')':
            # print("found )")
            while stack and stack[-1] != '(':
                # print(f"removing {stack[-1]} from stack")
                output += stack.pop()
                # print("output: ", output)
            # print(f'removing {stack[-1]} from stack')
            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                # print(f'removing {stack[-1]} from stack')
                output += stack.pop()
            # print(f"appending {character}")
            stack.append(character)

    while stack:
        # print(f"appending {stack[-1]}")
        output += stack.pop()

    return output


expression = "32*(2+5)*10"

print('infix notation: ', expression)

print('postfix notation: ', infixToPostfix(expression))
