line = int(input())

def solution(statement):
    s = list()
    cnt = 0
    for ch in statement:
        if ch == '(':
            s.append(ch)
            cnt += 1
        elif ch == ')':
            if len(s) == 0:
                print("NO")
                return False
            else:
                left = s.pop()
                if left != '(':
                    print("NO")
                    return False
    if len(s) != 0:
        print("NO")
    elif cnt < 1:
        print("NO")
    elif len(s) == 0:
        print("YES")

for i in range(line):
    solution(input())