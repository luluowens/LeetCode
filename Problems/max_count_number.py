'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        values = {}
        
        def get_key(val):
            for key, value in values.items():
                if val == value:
                    return key
                
        for i in range(len(nums)) :
            if nums[i] not in values :
                values[nums[i]] = 1
            else :
                values[nums[i]] += 1
        count = values.values()
        return get_key(max(count))


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.majorityElement([3,2,3]), 3)
        self.assertEqual(my_sol.majorityElement([2,2,1,1,1,2,2]), 2)
        self.assertEqual(my_sol.majorityElement([2,2,2,2]), 2)
        self.assertEqual(my_sol.majorityElement([1,1,1,1,2,2]), 1)
        

if __name__ == '__main__':
    unittest.main()