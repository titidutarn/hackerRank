def isBalanced(sentence):
    stack = []
    for s in sentence:
        if s in d.values():
            stack.append(s)
        elif s in d.keys():
            if stack.pop() != d[s]:
                return False
        else:
            return False
    return True if not len(stack) else False

d = {'}':'{',']':'[',')':'('}
sentence = input()
print(isBalanced(sentence))
