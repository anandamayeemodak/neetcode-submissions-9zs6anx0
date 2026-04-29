class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0:
            return ""

        lp = s[0]

        for i in range(len(s)):
            l, r = i-1, i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                lp = s[l:r+1] if len(lp) < len(s[l:r+1]) else lp

                l -= 1
                r += 1

            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                lp = s[l:r+1] if len(lp) < len(s[l:r+1]) else lp

                l -= 1
                r += 1
        
        return lp

        