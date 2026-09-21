class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        d = {}

        for a, b in zip(pattern, words):
            if a in d and d[a] != b:
                return False
            if b in d.values() and a not in d:
                return False
            d[a] = b

        return True