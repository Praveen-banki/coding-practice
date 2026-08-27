class Solution:
    def hammingWeight(self, n: int) -> int:
        m = bin(n)[2:]
        c = 0
        for i in m:
            if i=='1':
                c += 1
        return c