from BinarySearchTree.binary_search_tree import Solution, TreeNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node0 = TreeNode(4, None, None)
        node1 = TreeNode(2, None, None)
        node2 = TreeNode(7, None, None)
        node3 = TreeNode(1, None, None)
        node4 = TreeNode(3, None, None)
        node0.left = node1
        node0.right = node2
        node1.left = node3
        node1.right = node4
        my_solution = Solution()
        self.assertEqual(node1, my_solution.searchBST(node0, 2))

if __name__ == '__main__':
    unittest.main()
