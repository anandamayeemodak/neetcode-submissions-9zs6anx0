import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = Counter(tasks)
        max_heap = [cnt for cnt in task_count.values()]
        
        heapq.heapify_max(max_heap)
        queue = deque([])

        time = 0

        while max_heap or queue:
            time += 1

            #pop from max_heap and process task
            if not max_heap:
                time = queue[0][1]
            
            else:
                task = heapq.heappop_max(max_heap)
                task -= 1

                if task > 0:
                    queue.append([task, (n+time)])

            
            if queue and queue[0][1] == time:
                reappend_task = queue.popleft()[0]
                heapq.heappush_max(max_heap, reappend_task)
                
        return time
            


