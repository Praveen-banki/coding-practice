class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = [[]]

        for i in range(1, n + 1):
            ans += [x + [i] for x in ans if len(x) < k]

        return [x for x in ans if len(x) == k]