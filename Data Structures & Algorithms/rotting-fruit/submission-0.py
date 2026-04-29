from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        visited = set()
        queue = deque()

        n, m = len(grid), len(grid[0])

        def updateAdj(i, j, n, m):
            if i<0 or j<0 or i>=n or j>=m or (i,j) in visited or grid[i][j]==0:
                return
            
            visited.add((i,j))
            queue.append((i,j))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.append([i,j])
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                else:
                    continue

        adj = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = adj
                updateAdj(r+1, c, n, m)
                updateAdj(r, c+1, n, m)
                updateAdj(r-1, c, n, m)
                updateAdj(r, c-1, n, m)

            adj -= 1
        
        time = 0
        for fruit in fresh:
            i, j = fruit[0], fruit[1]
            if grid[i][j] == 1:
                return -1
            else:
                time = max(time, abs(grid[i][j]))

        return time
            


        