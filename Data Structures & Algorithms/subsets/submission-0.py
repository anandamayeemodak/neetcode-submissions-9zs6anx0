class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        comb = []

        def backtrack(i):
            if i >= len(nums):
                subsets.append(comb[:])
                return
            
            comb.append(nums[i])
            backtrack(i+1)

            comb.pop()
            backtrack(i+1)

        backtrack(0)

        return subsets 

            

        