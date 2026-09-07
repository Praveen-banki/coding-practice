from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = {()}

        for n in nums:
            ans = {p[:i] + (n,) + p[i:] 
                   for p in ans 
                   for i in range(len(p) + 1)}

        return [list(p) for p in ans]