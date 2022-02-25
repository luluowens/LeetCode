from AddTwoNumbers.add_two_numbers import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        # node0 = ListNode(1)
        # node1 = ListNode(2)
        # node2 = ListNode(3)
        # node3 = ListNode(4)
        # node4 = ListNode(5)
        # node0.next = node1
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # self.assertEqual(Solution().oddEvenList(node0), node0)
        # self.assertEqual(node0.next, node2)
        # self.assertEqual(node2.next, node4)
        # self.assertEqual(node1.next, node3)
        # self.assertEqual(node3.next, None)
        # self.assertEqual(node4.next, node1)


        node0 = ListNode(2)
        node1 = ListNode(4)
        node2 = ListNode(3)
        node3 = ListNode(5)
        node4 = ListNode(6)
        node5 = ListNode(4)
        node0.next = node1
        node1.next = node2
        node3.next = node4
        node4.next = node5
        nodeNew = Solution().addTwoNumbers(node0, node3)
        self.assertEqual(nodeNew.val, 7)
        self.assertEqual(nodeNew.next.val, 0)
        self.assertEqual(nodeNew.next.next.val, 8)


if __name__ == '__main__':
    unittest.main()
