class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            new_target = target - nums[i]
            j = (nums[i+1:].index(new_target) + i + 1) if new_target in nums[i+1:] else None

            if j:
                return [i, j]
            

        