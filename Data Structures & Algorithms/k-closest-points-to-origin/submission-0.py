import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            dist = (point[0]**2) + (point[1]**2)
            print(dist)
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (dist, point))
            else:
                heapq.heappushpop_max(max_heap, (dist, point))
        
        
        res = [point[1] for point in max_heap[:k]]

        return res

        