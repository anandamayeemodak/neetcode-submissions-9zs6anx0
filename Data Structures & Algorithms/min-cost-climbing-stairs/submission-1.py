class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1]*(len(cost))

        def rec_minCostClimbingStairs(pos):
            if pos >= len(cost):
                return 0
            
            if dp[pos] != -1:
                return dp[pos]
            
            dp[pos] = cost[pos] + min(rec_minCostClimbingStairs(pos+1), rec_minCostClimbingStairs(pos+2))

            return dp[pos]
        
        res1 = rec_minCostClimbingStairs(0)
        res2 = rec_minCostClimbingStairs(1)

        


        return min(res1, res2)