from RemoveValsLinkedList.remove_vals_linked_list import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        # node0 = ListNode(6)
        # node1 = ListNode(1)
        # node2 = ListNode(2)
        # node3 = ListNode(6)
        # node4 = ListNode(3)
        # node5 = ListNode(4)
        # node6 = ListNode(5)
        # node7 = ListNode(6)
        # node0.next = node1
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # node4.next = node5
        # node5.next = node6
        # node6.next = node7
        # self.assertEqual(Solution().removeElements(node0, 6), node1)
        # self.assertEqual(node2.next, node4)
        # self.assertEqual(node6.next, None)

        # node0 = ListNode(7)
        # node1 = ListNode(7)
        # node2 = ListNode(7)
        # node3 = ListNode(7)
        # node0.next = node1
        # node1.next = node2
        # node2.next = node3
        # self.assertEqual(Solution().removeElements(node0, 7), None)
        
        node0 = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(2)
        node3 = ListNode(1)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        self.assertEqual(Solution().removeElements(node0, 2), node0)
        self.assertEqual(node0.next, node3)


if __name__ == '__main__':
    unittest.main()
