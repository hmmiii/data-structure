def printReverse(msg, len):
    if len>0:
        print(msg[len-1])
        printReverse(msg, len-1)

instr = "자료구조"
printReverse(instr, len(instr))
print()