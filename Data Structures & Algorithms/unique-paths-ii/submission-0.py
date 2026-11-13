class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        dp = {(row -1 , col -1):1}

        def dfs(r,c):

            if r == row or c == col or grid[r][c] == 1:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r+1 ,c) + dfs(r,c+1)
            return dp[(r,c)]
        
        return dfs(0,0)