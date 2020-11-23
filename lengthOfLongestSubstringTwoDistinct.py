class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        longest = 0
        i = 0
        j = 0
        ld = 0
        check = set()

        while j < len(s):
            if len(check) < 1:
                check.add(s[i])
                longest = max(longest, j - i + 1)
                j += 1
            elif len(check) < 2:
                check.add(s[j])
                longest = max(longest, j - i + 1)
                ld = j
                j += 1
            else:
                if s[j] in check:
                    longest = max(longest, j - i + 1)
                    j += 1
                else:
                    i = ld
                    j = ld
                    check = set()
        
        return longest