# 링 버퍼 테스트 프로그램
from circleQueue import CircleQueue

q = CircleQueue(8) # 큐 객체 생성(capacuty=8)

q.display("초기 상태")
for i in range(6): # enqueue2(): 0, 1, 2, 3, 4, 5
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6); q.enqueue2(7) # enqueue2(): 6, 7
q.display("삽입 6,7") # 이제 큐는 포화상태

q.enqueue2(8); q.enqueue2(9) # 포화상태에서 두 번의 삽입 연산 수행. 가장 오래된 요소 2개 삭제.
q.display("삽입 8,9")

q.dequeue(); q.dequeue() # dequeue() 2회
q.display("삭제 x2")