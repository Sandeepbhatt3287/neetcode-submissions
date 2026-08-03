class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islands = 0
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(i,j):

            if  (i<0 or j<0 or i >= row or j >= col or grid[i][j]=="0"):
                return
            
            grid[i][j] = "0"

            for r,c in dir:
                dfs(i+r, j+c)


        for i in range(row):
            for j in range(col):
                if grid[i][j]!="0":
                    dfs(i,j)
                    islands +=1
        
        return islands