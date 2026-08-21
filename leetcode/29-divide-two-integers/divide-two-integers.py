class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        neg = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        ans = 0

        while a >= b:
            temp = b
            count = 1

            while a >= temp + temp:
                temp += temp
                count += count

            a -= temp
            ans += count

        if neg:
            ans = 0 - ans

        return ans