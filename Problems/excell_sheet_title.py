'''Given an integer columnNumber, return its corresponding column title
as it appearsin an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0 :
            ans += chr((columnNumber - 1) % 26 + 65)
            columnNumber = (columnNumber - 1) // 26
        return ans[::-1]


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.convertToTitle(1), "A")
        self.assertEqual(my_sol.convertToTitle(26), "Z")
        self.assertEqual(my_sol.convertToTitle(28), "AB")
        self.assertEqual(my_sol.convertToTitle(701), "ZY")
        

if __name__ == '__main__':
    unittest.main()