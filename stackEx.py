# 스택 예제, 괄호 검사 프로그램.

class ArrayStack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity # 스택 용량
        self.array = [None] * capacity # 요소 배열
        self.top = -1
    
    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity-1

    def push(self,item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else : pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek(self):
        if not self.isEmpty(): return self.array[self.top]
        else: pass
    
    def size(self): return self.top+1

def checkBrakets(statement):
    stack = ArrayStack(100) # 공백 상태 스택 준비
    for ch in statement: # 문자열의 각 문자에 대해
        if ch in ('{', '[','('): # 열리는 괄호이면 스택에 삽입
            stack.push(ch)
        elif ch in('}', ']', ')'):
            if stack.isEmpty(): # 닫히는 괄호인데, 스택이 공백이면 오른쪽 괄호가 먼저 나온경우, 조건2 위반
                return False
            else:
                left = stack.pop() # 문자를 pop해서 비교
                # 쌍이 맞지 않는 경우. 조건3 위반.
                if  (ch == '}' and left != "{") or \
                    (ch == ']' and left != '[') or \
                    (ch == ')' and left != '('):
                    return False
                
    return stack.isEmpty() # 만약, 스택이 공백이면 True를 반환하고, 공백이 아니면 조건1을 위반한 경우이므로 False를 반환

print(checkBrakets("{A")) # False
print(checkBrakets("{A}")) # True