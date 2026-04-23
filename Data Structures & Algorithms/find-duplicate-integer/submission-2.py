class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # [1,3,4,2,2]

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] < 0:
                return (idx + 1)
            else:
                nums[idx] = nums[idx]*(-1)
        
        


        