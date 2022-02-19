# Definition for singly-linked list.
from operator import truediv
from pickle import TRUE


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self) -> bool:
        fast_curr = self.head
        slow_curr = self.head
        while fast_curr and fast_curr.next and slow_curr:
            fast_curr = fast_curr.next.next
            slow_curr = slow_curr.next
            if fast_curr == slow_curr :
                return True
        return False
