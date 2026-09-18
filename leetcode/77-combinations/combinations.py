class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        def solve(start, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                solve(i + 1, path)
                path.pop()

        solve(1, [])
        return ans
