class Solution:
    def climbStairs(self, n: int) -> int:
        self.ways = 0

        dp = [-1]*(n)
        
        def rec_climbStairs(pos):
            if pos == n:
                return 1
            if pos > n:
                return 0
            if dp[pos] != -1:
                return dp[pos]
            
            dp[pos] = rec_climbStairs(pos+1) + rec_climbStairs(pos+2)
            return dp[pos]
            
        return rec_climbStairs(0)

        

        