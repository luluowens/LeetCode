# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        list_vals = []
        while curr :
            list_vals.append(curr.val)
            curr = curr.next
        for x in range(len(list_vals) // 2 + 1) :
            if list_vals[x] != list_vals[len(list_vals) - x - 1] :
                return False
        return True
