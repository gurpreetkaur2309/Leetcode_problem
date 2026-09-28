class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            res = res + value * (i + 1)

        return res