# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        currA = list1
        currB = list2
        tempHead = ListNode()
        temp = ListNode()
        while currA and currB :
            if currA.val <= currB.val :
                if not tempHead :
                    tempHead = currA
                    tempHead.next = currB
                    temp = tempHead.next
                else :
                    temp.next = currA
                    temp.next.next = currB
                    
