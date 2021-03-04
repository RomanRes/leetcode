test = "abbaca"

def removeDuplicates(S: str) -> str:
    stack = []
    for letter in S:
        if stack and letter == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


print(removeDuplicates(test))


