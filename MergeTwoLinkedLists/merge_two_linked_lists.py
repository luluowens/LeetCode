# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        currA = list1
        currB = list2
        new = ListNode(0)
        head = ListNode(-101)
        while currA or currB :
            if currA and currB:
                if currA.val < currB.val :
                    new.next = currA
                    new = new.next
                    currA = currA.next
                else :
                    new.next = currB
                    new = new.next
                    currB = currB.next
            elif currA :
                new.next = currA
                new = new.next
                currA = currA.next
            elif currB :
                new.next = currB
                new = new.next
                currB = currB.next
            if head.val == -101 :
                head = new
        if head.val == -101 :
            return None
        else :
            return head
