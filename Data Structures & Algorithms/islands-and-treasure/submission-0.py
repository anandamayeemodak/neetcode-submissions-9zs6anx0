from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        queue = deque()

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        def neighbors(i, j, n, m):
            if i<0 or j<0 or i>=n or j>=m or (i,j) in visited or grid[i][j] == -1:
                return
            
            visited.add((i,j))
            queue.append((i,j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                neighbors(r+1, c, n, m)
                neighbors(r, c+1, n, m)
                neighbors(r-1, c, n, m)
                neighbors(r, c-1, n, m)

            dist+=1




        