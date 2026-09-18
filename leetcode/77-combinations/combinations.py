class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        def f(start, a):
            if len(a) == k:
                ans.append(a[:])
                return
            for i in range(start, n + 1):
                f(i + 1, a + [i])

        f(1, [])
        return ans