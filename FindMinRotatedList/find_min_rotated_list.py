class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1] :
            return nums[0]
        else :
            left = 0
            right = len(nums) - 1
            while left < right :
                inflect = (right + left) // 2
                if nums[inflect] < nums[inflect + 1] :
                    if nums[inflect] > nums[inflect - 1] :
                        if nums[inflect] < nums[-1] :
                            right = inflect - 1
                        else :
                            left = inflect + 1
                    else :
                        return nums[inflect]
                else :
                    inflect += 1
                    return nums[inflect]

# nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
nums = [2, 1]
mySol = Solution()
print(mySol.findMin(nums))