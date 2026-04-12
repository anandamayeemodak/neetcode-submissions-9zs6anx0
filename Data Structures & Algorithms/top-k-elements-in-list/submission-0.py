import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        min_heap = []

        for num in nums_set:
            count_i = nums.count(num)
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (count_i, num))
            else:
                heapq.heappush(min_heap, (count_i, num))
        
        res = []

        for (freq, num) in min_heap:
            res.append(num)

        return res


        

        