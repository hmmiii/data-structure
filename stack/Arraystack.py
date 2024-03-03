class ArrayStack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity # 스택 용량
        self.array = [None] * capacity # 요소 배열
        self.top = -1
    
    def isEmpty(self) -> bool : return self.top == -1
    def isFull(self) -> bool : return self.top == self.capacity-1

    def push(self,item) -> None:
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else : pass

    def pop(self) -> any:
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek(self) -> any:
        if not self.isEmpty(): return self.array[self.top]
        else: pass
    
    def size(self) -> int : return self.top+1

    def clear(self) -> None:
        self.top = -1

    def display(self) -> None:
        print("[ ", end='')
        for i in range(self.top+1):
            print(" %s " % self.array[i], end='')
        print(" ]", end='')
        print()
