from LinkedListCycle.linked_list_cycle_ii import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        # # With cycle
        # node1 = ListNode(3)
        # node2 = ListNode(2)
        # node3 = ListNode(0)
        # node4 = ListNode(-4)
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # node4.next = node2
        # self.assertEqual(Solution.detectCycle({node1, node2, node3, node4}, node1), node2)

        # Without cycle
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        self.assertEqual(Solution.detectCycle({node1, node2, node3, node4}, node1), None)

if __name__ == '__main__':
    unittest.main()
