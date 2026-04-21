class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        cur_min = float('inf')
        
        while l<=r:
            m = (l+r)//2

            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                cur_min = min(cur_min, nums[l])

            if nums[l] <= nums[m]:
                #in the left sorted array so search right
                l = m+1
                cur_min = min(cur_min, nums[l]) if l<len(nums)-1 else cur_min
            else:
                #in the right sorted array so search left
                r = m-1
        
        return cur_min

        