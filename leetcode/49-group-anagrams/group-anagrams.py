class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key, []).append(s)

        return list(d.values())