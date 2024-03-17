arr = list()
def solution(num):
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

inputs = list()

lines = int(input())

for _ in range(lines):
    inputs.append(int(input()))

for input in inputs:
    solution(input)

print(sum(arr))