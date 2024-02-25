# 원형 큐를 배열로 구현.

class CircleQueue:
    def __init__(self, capacity = 10) -> None: # 생성자 정의
        self.capacity = capacity # 용량(고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스
    
    def isEmpty(self): # 공백 상태
        return self.front == self.rear
    
    def isFull(self): # 포화 상태
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self,item): # 삽입 연산
        if not self.isFull(): # 포화 상태가 아닌 경우
            self.rear = (self.rear+1) % self.capacity
            self.array[self.rear] = item
        else : pass
    
    def enqueue2(self, item): # 링 버퍼 삽입 연산
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item # 일단, 무조건 삽입
        if self.isEmpty(): # front == rear
            self.front = (self.front + 1) % self.capacity
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.capacity
            return self.array[self.front]
        else: pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1) % self.capacity]
        else : pass
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self,msg='목록'):
        print(msg, end=' = [ ')
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i%self.capacity], end =' ')
        print("]")