class Solution:
    def countSubstrings(self, s: str) -> int:
        subs_count = len(s)

        for i in range(0, len(s)):
            l, r = i-1, i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                subs_count += 1
                l -= 1
                r += 1
            
            l, r = i, i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                subs_count += 1
                l -= 1
                r += 1

        return subs_count
        
        