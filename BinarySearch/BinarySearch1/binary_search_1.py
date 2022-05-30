class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ind = len(nums) // 2
        ans = 0
        while 0 < ind and ind < len(nums) :
            if nums[ind] < target :
                ans += ind
                nums = nums[ind : len(nums)]
                ind = len(nums) // 2
            elif nums[ind] > target :
                nums = nums[0 : ind]
                ind = len(nums) // 2
            else :
                ans += ind
                return ans
        if ind == 0 :
            if nums[0] == target :
                return 0
            else :
                return -1