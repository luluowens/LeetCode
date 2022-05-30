import bisect

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == k:
            return arr
        # left = 0
        # right = len(arr) - 1
        # distance = len(arr) - 1
        # # while left <= right :
        #     mid = int((left + right) / 2)
        #     if abs(mid - x) <= distance :
        #         distance = abs(mid - x)
        #     if arr[mid] < x :
        #         left = mid + 1
        #     elif arr[mid] > x :
        #         right = mid - 1
        #     else :
        #         break
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]
