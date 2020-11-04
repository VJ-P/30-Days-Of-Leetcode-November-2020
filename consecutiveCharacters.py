class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        maxL = 1
        currL = 1
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                currL += 1
                maxL = max(currL, maxL)
            else:
                currL = 1
                prev = s[i]
        return maxL