class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = []
        zero = []

        for i in nums:
            if i != 0:
                non_zero.append(i)
            else:
                zero.append(i)

        nums[:] = non_zero + zero