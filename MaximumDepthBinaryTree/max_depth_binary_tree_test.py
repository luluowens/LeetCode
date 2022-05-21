from MaximumDepthBinaryTree.max_depth_binary_tree import Solution, TreeNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node0 = TreeNode(3, None, None)
        node1 = TreeNode(9, None, None)
        node2 = TreeNode(20, None, None)
        node3 = TreeNode(15, None, None)
        node4 = TreeNode(7, None, None)
        node0.left = node1
        node0.right = node2
        node2.left = node3
        node2.right = node4
        my_solution = Solution()
        self.assertEqual(3, my_solution.maxDepth(node0))

if __name__ == '__main__':
    unittest.main()
