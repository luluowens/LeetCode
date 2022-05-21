# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            max_length = 1
            if root.right or root.left :
                left_length = self.maxDepth(root.left)
                right_length = self.maxDepth(root.right)
                if right_length >= left_length :
                    max_length += right_length
                else :
                    max_length += left_length
        else :
            max_length = 0
        return max_length