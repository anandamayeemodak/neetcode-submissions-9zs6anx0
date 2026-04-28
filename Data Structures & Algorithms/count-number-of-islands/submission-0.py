class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n, m = len(grid), len(grid[0])
        self.visited = set()

        def dfs(i, j, n, m):
            if i<0 or j<0 or i>=n or j>=m or ((i,j) in self.visited) or grid[i][j]=="0":
                return

            self.visited.add((i,j))

            dfs(i, j+1, n, m)
            dfs(i+1, j, n, m)
            dfs(i-1, j, n, m)
            dfs(i, j-1, n, m)
            





        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in self.visited:
                    islands += 1
                    dfs(i, j, n, m)

        return islands
        