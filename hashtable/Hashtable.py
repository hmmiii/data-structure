class Students():
    def __init__(self,length = 10) -> None:
        self.table = [None] * length

    def setValue(self, stuednt):
        self.table[stuednt['num'] % 9] = stuednt['name']
    
    def getValue(self, num) -> str:
        return self.table[num % 9]
    
    def printTable(self):
        for idx,val in enumerate(self.table):
            print(f'{idx} -> {val}')

students = Students(20)

students.setValue({'num':123123, 'name':'John'})
students.setValue({'num':521341, 'name':'Kim'})
students.setValue({'num':531641, 'name':'Lee'})

print(students.getValue(123123))
print(students.getValue(521341))
print(students.getValue(531641))

students.printTable()