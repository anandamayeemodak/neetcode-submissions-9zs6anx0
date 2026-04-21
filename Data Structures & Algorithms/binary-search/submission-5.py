# Sorted array -> Intuition is binary search
# start from first and last position and calculate the mid-point
# move l or r depending on [m] <> target else return m
# as soon as l > r, l has crossed r and we have eliminated all elements from consideration. 
# in this case return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

        