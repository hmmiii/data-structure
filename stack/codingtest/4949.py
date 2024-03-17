str = None
inputs = list()

while str != '.':
    str = input()
    if str != '.':
        inputs.append(str)

def solution(statement):
    arr = list()
    for char in statement:
        if char in ('(', '['):
            arr.append(char)
        elif char in(')', ']'):
            if len(arr) == 0:
                print('no')
                return False
            else:
                left = arr.pop()
                if char == ')' and left != '(' or \
                char == ']' and left != '[':
                    print('no')
                    return False
    
    if len(arr) != 0:
        print('no')
    else:
        print('yes')

for input in inputs:
    solution(input)