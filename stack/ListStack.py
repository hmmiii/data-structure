s = list() # 리스트를 객체를 생성해 스택으로 사용

msg = input("문자열 입력: ")
for c in msg:
    s.append(c) # c를 스택에 삽입

print("문자열 출력 : ", end='')
print()

print("사이즈 : ", len(s))

print("마지막 요소 : ", s[-1])

while len(s) > 0: # 스택이 공백이 아니라면
    print(s.pop(), end='')
print()
print("사이즈 : ", len(s))