class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right :
            val_sum = numbers[left] + numbers[right]
            if val_sum == target :
                return [left + 1, right + 1]
            elif val_sum < target :
                left += 1
            else :
                right -= 1