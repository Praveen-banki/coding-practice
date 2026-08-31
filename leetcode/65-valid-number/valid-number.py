class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if "e" in s.lower():
                a, b = s.lower().split("e")
                if "." in b:
                    return False
                int(b)

            else:
                a = s

            float(a)

            if "inf" in s.lower() or "nan" in s.lower():
                return False

            return True

        except:
            return False