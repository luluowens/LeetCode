# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        while curr and curr.next :
            if head.val == val :
                head = head.next
                curr = curr.next
            elif curr.next.val == val :
                if curr.next.next :
                    curr.next = curr.next.next
                else :
                    curr.next = None
            else :
                curr = curr.next
        if curr :
            if curr.val == val :
                head = None
        return head
