def parenthesis(s):

    if len(s) %2 != 0:
        return False

    opening = set('([{')
    match = set([('{','}'),('[',']'),('(',')')])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            else:
                open_match = stack.pop()

                if (open_match,paren) not in match:
                    return False

    if len(stack) == 0:
        return True

p = parenthesis('[{}]')
print(p)

