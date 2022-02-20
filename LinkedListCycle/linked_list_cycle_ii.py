# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        ids = set()
        while curr :
            if curr.next not in ids :
                ids.add(curr)
                curr = curr.next
            else :
                return curr.next
        return None
