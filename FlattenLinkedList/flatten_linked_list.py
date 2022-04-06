# Definition for a Node.


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    # def flatten(self, head: Node) -> Node :
    #     curr = head
    #     while curr.next :
    #         if curr.child :
    #             child = curr.child
    #             curr.next = curr.child
    #             curr.child.prev = curr
    #             curr.child = None
    #             curr = self.flatten(child)
    #         else :
    #             curr = curr.next
    #     return curr

    def flatten_child(self, head: Node) -> Node :
        curr = head
        while curr and curr.next :
            if curr.child :
                temp = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                curr = curr.next
                curr = self.flatten_child(curr.child)
            elif curr.next.next == None and temp != None:
                curr.next.next = temp
                temp.prev = curr.next.next
                temp = None
            else :
                curr = curr.next
        return curr


    def flatten(self, head: Node) -> Node :
        curr = head
        while curr and curr.next :
            if curr.child :
                curr = self.flatten_child(curr.child)
            else :
                curr = curr.next
        return head


        # curr = head
        # while curr :
        #     if curr.child :
        #         curr.next = curr.child
        #         curr.child.prev = curr
        #         curr.child = None
        #         curr = self.flatten_child(curr.child)
        #     curr = curr.next
        # return head
        