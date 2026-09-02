class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                x = int(num1[i]) * int(num2[j])
                x += res[i+j+1]

                res[i+j+1] = x % 10
                res[i+j] += x // 10

        return ''.join(map(str, res)).lstrip('0')