class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

fst = Node(1)
scd = Node(2)
trd = Node(3)

fst.next = scd
trd.next = trd

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self, value) -> None:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = newNode
    def delete_after(self) -> None:
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            ptr = self.head
            while ptr.next.next: # 다음 요소의 다음 요소가 존재하지 않을때까지(마지막-1번째 요소까지) 반복.
                ptr = ptr.next
            ptr.next = None
    def print(self) -> None:
        ptr = self.head
        while ptr.next:
            print(f'{ptr.value} -> {ptr.next.value}')
            ptr = ptr.next

linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.delete_after()
linkedlist.print()