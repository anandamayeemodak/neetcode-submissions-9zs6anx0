class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        cur = []

        def backtrack(i):
            if sum(cur) == target and cur not in combinations:
                combinations.append(cur[:])

            if i >= len(nums) or sum(cur) > target:
                return
            
            cur.append(nums[i])
            backtrack(i)

            cur.pop()
            backtrack(i+1)

        
        backtrack(0)

        return combinations
