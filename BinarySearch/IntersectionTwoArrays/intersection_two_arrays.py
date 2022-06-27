class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        for i in range(len(nums1)) :
            # left = 0
            # right = nums2
            for j in range(len(nums2)) :
                if nums1[i] == nums2[j] :
                    if nums1[i] not in intersection :
                        intersection.append(nums1[i])
        return intersection