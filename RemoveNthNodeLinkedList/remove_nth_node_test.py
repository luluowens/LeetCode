from RemoveNthNodeLinkedList.remove_nth_node import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        self.assertEqual(Solution.removeNthFromEnd({node1, node2, node3, node4, node5}, node1, 2), node1)


if __name__ == '__main__':
    unittest.main()
