class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num11 = set(nums1)
        num22 = set(nums2)
        return list(num11 & num22)