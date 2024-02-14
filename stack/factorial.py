# 팩토리얼 : 1부터 n까지 곱한 값, n!
# n!은 (n-1)!에 n을 곱하면 된다.


def factorial_iter(n): # 반복 구조로 구현한 팩토리얼
    result = 1
    for k in range(2, n+1): # k:2, ..., n
        result = result * k # result에 k를 곱함.
    return result

print("반복 구조 팩토리얼 : ", end='')
print(factorial_iter(5))

def factorial(n): # 순환구조(재귀호출)로 구현한 팩토리얼.
    if n == 1:
        return 1 # 순환 호출을 멈추는 부분. n이 1이면 답을 알고 있음.
    else:
        return n * factorial(n-1) # 자신을 순환적으로 호출하는 부분. 문제의 크기는 작아져야 함.
    
print("순환 구조 팩토리얼 : ", end='')
print(factorial(5))