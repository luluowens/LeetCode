class MyNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index :
                return curr.val
            else:
                count += 1
                curr = curr.next
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        new = MyNode(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = MyNode(val)
        curr = self.head
        while curr and curr.next :
            curr = curr.next
        if not curr :
            curr = new
            self.head = new
        elif not curr.next :
            curr.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        new = MyNode(val)
        count = 0
        curr = self.head
        if index == 0:
            self.addAtHead(val)
        else :
            while curr and curr.next and count <= index - 1:
                if count == index - 1 :
                    new.next = curr.next
                    curr.next = new
                curr = curr.next
                count += 1
            if curr and not curr.next:
                self.addAtTail(val)


    def deleteAtIndex(self, index: int) -> None:
        count = 0
        curr = self.head
        if index == 0 :
            self.head = curr.next
        else :
            while curr and curr.next and count <= index - 1:
                temp = curr.next
                if count == index-1 :
                    if temp.next :
                        curr.next = temp.next
                    else :
                        curr.next = None
                count += 1
                curr = curr.next

