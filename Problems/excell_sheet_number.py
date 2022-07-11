class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle)
        for i in range(length) :
            ans += (ord(columnTitle[length - i - 1]) - 64)* pow(26, i)
        return ans


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.titleToNumber("A"), 1)
        self.assertEqual(my_sol.titleToNumber("Z"), 26)
        self.assertEqual(my_sol.titleToNumber("AB"), 28)
        self.assertEqual(my_sol.titleToNumber("ZY"), 701)
        

if __name__ == '__main__':
    unittest.main()