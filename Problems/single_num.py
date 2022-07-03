'''Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        nums.append(None)
        i = 0
        while i < len(nums) :
            if nums[i] == nums[i+1] :
                i += 2
            else :
                return nums[i]



import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.singleNumber([2,2,1]), 1)
        self.assertEqual(my_sol.singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(my_sol.singleNumber([1]), 1)
        

if __name__ == '__main__':
    unittest.main()