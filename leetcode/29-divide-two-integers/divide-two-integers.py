class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)

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

        if negative:
            ans = 0 - ans

        if ans > 2147483647:
            return 2147483647

        if ans < -2147483648:
            return -2147483648

        return ans