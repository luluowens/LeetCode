class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high :
            mid = low + (high - low) // 2
            if nums[mid] < target :
                low = mid + 1
            elif nums[mid] > target :
                high = mid - 1
            else :
                if mid == 0 :
                    return 0
                elif nums[mid-1] == target :
                    high = mid - 1
                else :
                    return mid
        mid = low + (high - low) // 2
        if mid < 0 :
            return 0
        elif nums[mid] < target :
            return mid + 1
        elif nums[mid] >= target :
            return mid