# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        currA = head
        currB = head
        count = 0
        while currA and currB :
            if count < n :
                currB = currB.next
                count += 1
            elif currB.next :
                currA = currA.next
                currB = currB.next
            else:
                if n == 1:
                    currA.next = None
                    return head
                else :
                    currA.next = currA.next.next
                    return head
        head = head.next
        return head
