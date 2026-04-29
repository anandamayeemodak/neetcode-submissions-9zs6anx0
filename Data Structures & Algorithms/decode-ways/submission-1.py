class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [-1]*(len(s))

        def rec_spliting(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = rec_spliting(i+1)
            if i < len(s)-1:
                if int(s[i:i+2]) < 27:
                    dp[i] += rec_spliting(i+2)
            

            return dp[i]

        return rec_spliting(0)
        