# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        vals = set()
        while currA :
            vals.add(currA)
            currA = currA.next
        while currB :
            if currB in vals :
                return currB
            currB = currB.next
        return None
