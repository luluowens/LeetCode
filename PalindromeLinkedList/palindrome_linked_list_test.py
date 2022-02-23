from PalindromeLinkedList.palindrome_linked_list import Solution, ListNode
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        node0 = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(2)
        node4 = ListNode(0)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        self.assertEqual(Solution().isPalindrome(node0), False)



        # node0 = ListNode(1)
        # node1 = ListNode(2)
        # node2 = ListNode(3)
        # node3 = ListNode(3)
        # node4 = ListNode(2)
        # node5 = ListNode(1)
        # node0.next = node1
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # node4.next = node5
        # self.assertEqual(Solution().isPalindrome(node0), True)



if __name__ == '__main__':
    unittest.main()
