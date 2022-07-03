'''Given an integer numRows, return the first numRows of Pascal's triangle.
'''
import operator as op
from functools import reduce

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        cache = []
        
        def nCr(n, r) :
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer // denom

        for num in range(numRows) :
            row = [nCr(num,i) for i in range(num+1)]
            cache.append(row)
        
        return cache


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.generate(1), [[1]])
        self.assertEqual(my_sol.generate(2), [[1], [1,1]])
        self.assertEqual(my_sol.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        

if __name__ == '__main__':
    unittest.main()