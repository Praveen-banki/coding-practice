class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2**32

        if num == 0:
            return "0"

        h = "0123456789abcdef"
        ans = ""

        while num:
            ans = h[num % 16] + ans
            num //= 16

        return ans