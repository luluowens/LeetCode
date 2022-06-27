class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        i = 0
        end = len(nums)
        while i < end :
            if nums[i] == val :
                nums.remove(val)
                nums.append(val)
                end -= 1
            else :
                count += 1
                i += 1
        return nums[:count]

s = Solution()
print(s.removeElement([3,2,2,3], 3))