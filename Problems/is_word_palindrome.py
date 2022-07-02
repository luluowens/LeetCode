'''A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = [char for char in s if ((ord(char) >= 97 and ord(char) <= 121) or (ord(char) >= 48 and ord(char) <= 57))]
        return chars == chars[::-1]


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(my_sol.isPalindrome("race a car"), False)
        self.assertEqual(my_sol.isPalindrome("  "), True)
        self.assertEqual(my_sol.isPalindrome("0P"), False)
        

if __name__ == '__main__':
    unittest.main()