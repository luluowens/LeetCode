# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        curr = head
        count = 1
        first_even = ListNode()
        while curr and curr.next :
            if count == 2 :
                first_even = curr
            temp = curr.next
            curr.next = curr.next.next
            curr = temp
            count += 1
            if curr.next :
                if not curr.next.next and count % 2 == 1 :
                    curr.next = first_even
                    break
        if not curr :
            return head
        elif not curr.next and count < 2 :
            return head
        elif not curr.next and count == 2:
            head.next = curr
            return head
        elif not curr.next and count % 2 == 1 :
            curr.next = first_even
        return head
