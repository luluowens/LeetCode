# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode()
        listHead = new
        carry = 0
        currA = l1
        currB = l2
        sum = 0
        while currA or currB :
            if currA :
                sum += currA.val
                currA = currA.next
            if currB :
                sum += currB.val
                currB = currB.next
            new.next = ListNode((sum + carry) % 10)
            new = new.next
            carry = int((sum + carry)/10)
            sum = 0
        if carry != 0 :
            new.next = ListNode(carry % 10)
            new = new.next
        return listHead.next