from LinkedListCycle.linked_list_intersection import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        # # Test 1
        # node1 = ListNode(1)
        # node2 = ListNode(9)
        # node3 = ListNode(1)
        # node4 = ListNode(3)
        # node5 = ListNode(2)
        # node6 = ListNode(4)
        # node1.next = node2
        # node2.next = node3
        # node3.next = node5
        # node4.next = node5
        # node5.next = node6
        # self.assertEqual(Solution.getIntersectionNode({node1, node2, node3, node4, node5, node6}, node1, node4), node5)

        # Test 2
        node1 = ListNode(4)
        node2 = ListNode(1)
        node3 = ListNode(5)
        node4 = ListNode(6)
        node5 = ListNode(1)
        node6 = ListNode(8)
        node7 = ListNode(4)
        node8 = ListNode(5)
        node1.next = node2
        node2.next = node6
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        node7.next = node8
        self.assertEqual(Solution.getIntersectionNode({node1, node2, node3, node4, node5, node6, node7, node8}, node1, node3), node6)

if __name__ == '__main__':
    unittest.main()
