import queue # 파이썬 큐 모듈 포함

s = queue.LifoQueue(maxsize=100) # 스택 객체 생성(최대 크기 20), maxsize가 0이면 무한대임.

msg = input("문자열 입력 : ")
for c in msg:
    s.put(c) # c를 스택에 삽입

print("사이즈 : ", s.qsize())

print("마지막 요소 : ",s.queue[-1])

print("문자열 출력 : ", end='')
while not s.empty(): # 스택이 공백 상태가 아니라면
    print(s.get(), end='')
print()