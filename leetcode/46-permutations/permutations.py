class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        ans = []

        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]

            for p in self.permute(rest):
                ans.append(p + [nums[i]])

        return ans