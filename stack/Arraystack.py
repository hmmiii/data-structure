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


s = ArrayStack(100) # 새로운 스택 객체 생성.

# 문자열을 입력받아 msg에 저장하고, msg의 각 문자 c를 순서대로 스택에 삽입
msg = input("문자열 입력 : ")
for c in msg:
    s.push(c)
    
print("문자열 출력 : ", end='')

# 스택이 공백이 아니면 상단의 문자를 꺼내서 화면에 출력. 이 과정을 공백 상태가 될 때까지 반복
while not s.isEmpty():
    print(s.pop(), end ='')
print()
