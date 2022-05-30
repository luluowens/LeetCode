class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        target_left = self.findBound(nums, target, True)
        if (target_left == -1):
            return [-1, -1]
        target_right = self.findBound(nums, target, False)
        return [target_left, target_right]
        

    def findBound(self, nums: list[int], target: int, is_first: bool) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = int((left + right)  / 2)    
            if nums[mid] == target:
                if is_first:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1