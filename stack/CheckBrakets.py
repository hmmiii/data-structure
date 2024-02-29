from Arraystack import ArrayStack

def checkBrakets(statement:str) -> bool:
    """

    괄호를 검사하는 함수

    - 조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 합니다.
    - 조건 2 : 같은 종류인 경우 왼쪽 괄호가 오른쪽보다 먼저 나와야 합니다.
    - 조건 3 : 다른 종류의 괄호 쌍이 서로 교차하면 안 됩니다.
    
    Parameters:
    statement (str): 검사할 문장

    Returns:
    bool: 주어진 문장에 오류가 없으면 True, 있으면 False
    
    """
    
    stack = ArrayStack(100)

    for char in statement:
        if char in ('[', '{', '('):
            stack.push(char)
        elif char in (']', '}', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if char == ']' and left != '[' or \
                char == '}' and left != '{' or \
                char == ')' and left != '(':
                    return False
    return stack.isEmpty()

print(checkBrakets("{[a + b * (c - d)] / (e + f)}"))
print(checkBrakets("{[a + b * (c - d)] / (e + f}"))