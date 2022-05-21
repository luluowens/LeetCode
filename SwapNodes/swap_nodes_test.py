from swap_nodes import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node0 = ListNode(1, None)
        node1 = ListNode(2, None)
        node2 = ListNode(3, None)
        node3 = ListNode(4, None)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        my_solution = Solution()
        my_solution.swapPairs(node0)
        self.assertEqual(node1.next, node0)
        self.assertEqual(node0.next, node3)
        self.assertEqual(node3.next, node2)
        self.assertEqual(node2.next, None)

if __name__ == '__main__':
    unittest.main()
