# 원형 큐 테스트 프로그램
# 무작위로 발생한 정수(0~99)를 큐가 꽉 찰 때까지 삽입한 후, 다시 모든 숫자를 꺼내 출력하는 프로그램

from circleQueue import CircleQueue
import random

q = CircleQueue(8)

q.display("초기 상태")

while not q.isFull():
    q.enqueue(random.randint(0,100)) # 큐가 포화 상태가 될 때까지 0에서 99사이의 정수를 무작위로 발생호여 큐에 삽입. 용량이 8이므로 7개까지 삽입됨.

q.display("포화 상태")

print("삭제 순서 : ", end='')
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()
