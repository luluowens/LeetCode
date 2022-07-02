'''Given an integer numRows, return the first numRows of Pascal's triangle.
'''
import math

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # cache = []

        # for num in range(numRows) :
        #     if num == 0 :
        #         cache.append([1])
        #     else :
        #         row = []
        #         row.append(1)
        #         previous_row = cache[num - 1]
        #         for i in range(1, num) :
        #             row.append(previous_row[i-1] + previous_row[i])
        #         row.append(1)
        #         cache.append(row)

        cache = []

        for num in range(numRows) :
            row = []
            for i in range(num+1) :
                row.append(int(math.factorial(num) / (math.factorial(i) * math.factorial(num-i))))
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