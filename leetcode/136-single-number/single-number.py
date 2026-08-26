class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        new = []
        for i in nums:
            if i not in new:
                new.append(i)
            else:
                new.remove(i)
        return new[0]