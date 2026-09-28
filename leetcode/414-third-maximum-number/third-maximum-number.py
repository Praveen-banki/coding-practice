class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        num = list(set(nums))
        num.sort()

        if len(num) > 2:
            return num[-3]
        else:
            return num[-1]