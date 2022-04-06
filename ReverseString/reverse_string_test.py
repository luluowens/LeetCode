from reverse_string import Solution
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_solution = Solution()
        s = ["h","e","l","l","o"]
        rev_s = ["o","l","l","e","h"]
        my_solution.reverseString(s)
        self.assertEqual(s, rev_s)

        t = ["H","a","n","n","a","h"]
        rev_t = ["h","a","n","n","a","H"]
        my_solution.reverseString(t)
        self.assertEqual(t, rev_t)

if __name__ == '__main__':
    unittest.main()
