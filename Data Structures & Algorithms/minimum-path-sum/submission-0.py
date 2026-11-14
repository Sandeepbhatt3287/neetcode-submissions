class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        memo = [[-1] *col for _ in range(row)]

        def dfs(r,c):
            if r >= row or c >=col:
                return float('inf')
            
            if r == row-1 and c == col-1:
                return grid[r][c]
            
            if memo[r][c] != -1:
                return memo[r][c]

            down = dfs(r+1,c)
            right = dfs(r, c+1)

            best = grid[r][c] + min(down, right)

            memo[r][c] = best

            return memo[r][c]

        
        return dfs(0,0)