class Solution:
    def search(self, nums: list[int], target: int) -> int:
        import bisect

        i = nums.index(min(nums))
        nums = nums[i:] + nums[:i]

        j = bisect.bisect_left(nums, target)

        return (j + i) % len(nums) if j < len(nums) and nums[j] == target else -1