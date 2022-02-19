# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast_curr = head
        slow_curr = head
        while fast_curr and fast_curr.next and slow_curr:
            fast_curr = fast_curr.next.next
            slow_curr = slow_curr.next
            if fast_curr == slow_curr :
                return True
        return False
