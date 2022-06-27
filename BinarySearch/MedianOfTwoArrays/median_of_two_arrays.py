class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_list = nums1 + nums2
        new_list.sort()
        if len(new_list) % 2 == 1 :
            return 1.0 * (new_list[len(new_list) // 2])
        else :
            first_val = new_list[len(new_list) // 2]
            second_val = new_list[len(new_list) // 2 - 1]
            return (first_val + second_val) / 2

s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))