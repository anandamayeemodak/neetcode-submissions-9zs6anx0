class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        regions = []

        n, m = len(board), len(board[0])

        def dfs(i, j, n, m, cur_region):
            if i<0 or j<0 or i==n or j==m or (i,j) in visited or board[i][j] == "X":
                if len(cur_region)>0 and cur_region not in regions:
                    regions.append(cur_region)
                return
            
            cur_region.append([i, j])
            visited.add((i,j))

            dfs(i+1, j, n, m, cur_region)
            dfs(i, j+1, n, m, cur_region)
            dfs(i-1, j, n, m, cur_region)
            dfs(i, j-1, n, m, cur_region)
        
        def isSurrounded(region, n, m):
            print(region)
            for cell in region:
                i, j = cell[0], cell[1]     
                if i-1 < 0 or j-1 < 0 or i+1 == n or j+1 == m:
                    return False
                else:
                    o_count = [board[i+1][j], board[i][j+1], board[i-1][j], board[i][j-1]].count("O")
                    x_count = [board[i+1][j], board[i][j+1], board[i-1][j], board[i][j-1]].count("X")
                    if x_count >= 2 or (x_count==1 and o_count>2):
                        continue
                    else:
                        return False
            
            return True

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    cur_region = []
                    dfs(i, j, n, m, cur_region)
        
        for region in regions:
            if isSurrounded(region, n, m):
                for cell in region:
                    i, j = cell[0], cell[1]
                    board[i][j] = "X"
        

        