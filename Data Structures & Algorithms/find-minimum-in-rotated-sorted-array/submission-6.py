#Initial approach => go over array to find min(arr) or have consecutive pointers, p1 and p2 iterate as long as [p1] < [p2], moment it is otherwise, return [p2]
#Final approach => use binary search to check if m in left-sorted array or right-sorted array
                #  if m in left-sorted array, move l to right else move r to left
                #  store cur_min for [m] or [l] 

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

        