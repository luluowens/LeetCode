'''Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_vals = int(a) + int(b)
        sum_vals = str(sum_vals)[::-1]
        for i in range(len(sum_vals)) :
            digit = int(sum_vals[i])
            if digit > 1 :
                sum_vals = sum_vals[:i] + str(digit % 2) + sum_vals[i+1:]
                if i+1 < len(sum_vals) :
                    sum_vals = sum_vals[:i+1] + str(int(sum_vals[i+1]) + 1) + sum_vals[i+2:]
                else :
                    sum_vals += "1"
        return sum_vals[::-1]

# my_sol = Solution()
# # print(my_sol.addBinary("11", "1"))
# print(my_sol.addBinary("1010", "1011"))

import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.addBinary("11", "1"), "100")
        self.assertEqual(my_sol.addBinary("1010", "1011"), "10101")

if __name__ == '__main__':
    unittest.main()