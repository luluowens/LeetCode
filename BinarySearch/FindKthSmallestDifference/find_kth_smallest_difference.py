class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        def possible(guess) :
            count = 0
            left = 0
            for right, x in enumerate(nums) :
                while x - nums[left] > guess :
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right :
            mid = (left + right) / 2
            if possible(mid) :
                right = mid
            else:
                left = mid + 1

        return int(left)
