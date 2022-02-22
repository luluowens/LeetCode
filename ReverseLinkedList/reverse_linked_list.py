# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next :
            next = curr.next
            curr.next = next.next
            next.next = head
            head = next
        return head