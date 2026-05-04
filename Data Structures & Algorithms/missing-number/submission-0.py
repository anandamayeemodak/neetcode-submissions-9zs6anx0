class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        act_sum = sum(nums)
        exp_sum = n*(n+1)//2

        return abs(exp_sum - act_sum)