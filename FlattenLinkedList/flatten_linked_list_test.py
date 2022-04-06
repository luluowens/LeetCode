from FlattenLinkedList.flatten_linked_list import Solution, Node
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node1 = Node(1, None, None, None)
        node2 = Node(2, None, None, None)
        node3 = Node(3, None, None, None)
        node4 = Node(4, None, None, None)
        node5 = Node(5, None, None, None)
        node1.next = node2
        node2.prev = node1
        node1.child = node3
        node3.next = node4
        node4.next = node5
        node4.prev = node3
        node5.prev = node4
        # self.assertEqual(Solution().flatten_child(node1), node2)
        # self.assertEqual(node1.next, node3)
        # self.assertEqual(node2.next, None)
        # self.assertEqual(node3.next, node4)
        # self.assertEqual(node4.next, node5)
        # self.assertEqual(node5.next, node2)


        # node0 = ListNode(1)
        # node1 = ListNode(2)
        # node2 = ListNode(4)
        # node3 = ListNode(1)
        # node4 = ListNode(3)
        # node5 = ListNode(4)
        # node0.next = node1
        # node1.next = node2
        # node3.next = node4
        # node4.next = node5
        # self.assertEqual(Solution().mergeTwoLists(node0, node3), node0)


if __name__ == '__main__':
    unittest.main()
