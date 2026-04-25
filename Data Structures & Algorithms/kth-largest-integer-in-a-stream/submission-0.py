import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        if k < len(nums):
            nums = nums[(len(nums)-k):]

        self.k = k
        self.min_heap = nums
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]


        
