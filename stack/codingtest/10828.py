arr = list()
inputs = list()

def stack(line):
    cmds = line.split()

    cmd = cmds[0]
    if len(cmds) == 2:
        val = cmds[1]
    if cmd == 'push':
        arr.append(val)
    elif cmd == 'pop':
        if len(arr) == 0:
            return print(-1)
        print(arr.pop())
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if len(arr) <= 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(arr) == 0:
            return print(-1)
        print(arr[len(arr)-1])

lines = int(input())

for _ in range(lines):
    inputs.append(input())

for input in inputs:
    stack(input)
