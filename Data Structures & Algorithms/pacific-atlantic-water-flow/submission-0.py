class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        res = []

        n, m = len(heights), len(heights[0])

        def dfs(r, c, n, m, visited, prevH):
            if r<0 or c<0 or r>=n or c>=m or (r,c) in visited or heights[r][c]<prevH:
                return
            
            visited.add((r,c))
            dfs(r+1, c, n, m, visited, heights[r][c])
            dfs(r, c+1, n, m, visited, heights[r][c])
            dfs(r-1, c, n, m, visited, heights[r][c])
            dfs(r, c-1, n, m, visited, heights[r][c])

        for c in range(m):
            dfs(0, c, n, m, pac, heights[0][c])
            dfs(n-1, c, n, m, atl, heights[n-1][c])
        
        for r in range(n):
            dfs(r, 0, n, m, pac, heights[r][0])
            dfs(r, m-1, n, m, atl, heights[r][m-1])

        for r in range(n):
            for c in range(m):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res


        
        