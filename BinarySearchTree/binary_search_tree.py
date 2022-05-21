# Definition for a binary tree node.
class TreeNode :
    def __init__(self, val = 0, left = None, right = None) :
        self.val = val
        self.left = left
        self.right = right

class Solution :
    def searchBST(self, root: TreeNode, val: int) -> TreeNode :
        curr = root
        while curr :
            if curr.val == val :
                return curr
            elif curr.val < val :
                curr = curr.right
                return self.searchBST(curr, val)
            elif curr.val > val :
                curr = curr.left
                return self.searchBST(curr, val)
            else :
                return None
        return None
