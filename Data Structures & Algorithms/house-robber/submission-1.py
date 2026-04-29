class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums))
        
        def rec_rob(house):
            if house >= len(nums):
                return 0

            if dp[house] != -1:
                return dp[house]
            
            dp[house] = max(nums[house]+rec_rob(house+2), rec_rob(house+1))
            
            return dp[house]
        
        return rec_rob(0)