class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        cur = []

        def backtrack(i):
            if i >= len(nums):
                if sorted(cur[:]) not in subsets:
                    subsets.append(sorted(cur[:]))
                return

            cur.append(nums[i])
            backtrack(i+1)

            cur.pop()
            backtrack(i+1)

        backtrack(0)

        return subsets